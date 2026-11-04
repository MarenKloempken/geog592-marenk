print("Loading in Libraries")

import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages




url_0 = "https://www2.census.gov/geo/tiger/GENZ2024/shp/" # url for census tiger data 
url_county = "cb_2024_us_county_500k.zip" # county level
url_state = "cb_2024_us_state_500k.zip" # state level 



counties = gpd.read_file(url_0+url_county)
nc_counties = counties.loc[counties["STATEFP"] == "37"].to_crs(6543).copy()
nc_counties.plot(edgecolor="black", facecolor="white")


landfills = gpd.read_file("Active_Permitted_Landfills.geojson")

landfills = landfills.to_crs(nc_counties.crs)

print(nc_counties.columns)

print(nc_counties.crs)
print(landfills.crs)


landfills_by_county = gpd.sjoin(
    landfills,
    nc_counties[["NAME", "geometry"]],
    how="left",
    predicate="within"
)

landfill_counts = landfills_by_county.groupby("NAME").size()

nc_counties["landfill_count"] = (
    nc_counties["NAME"]
    .map(landfill_counts)
    .fillna(0)
    .astype(int)
)

print(nc_counties[["NAME", "landfill_count"]].head())



def county_map(county, ax):


    selected = nc_counties[nc_counties["NAME"] == county]

    selected.plot(
        ax=ax,
        edgecolor="black",
        facecolor="#7b9b90"
    )

    county_landfills = landfills_by_county[
        landfills_by_county["NAME"] == county
    ]

    county_landfills.plot(
        ax=ax,
        color="red",
        markersize=15
    )

    ax.set_title(f"{county} County Landfills")
    ax.set_axis_off()

    def locator_map(county, ax):

        selected = nc_counties[nc_counties["NAME"] == county]

        nc_counties.plot(
        ax=ax,
        edgecolor="gray",
        facecolor="white"
    )

        selected.plot(
        ax=ax,
        edgecolor="black",
        facecolor="#7b9b90"
    )

    ax.set_axis_off()



def county_figure(county, pdf):

    fig, axes = plt.subplots(
        2, 1,
        figsize=(8, 10),
        gridspec_kw={"height_ratios": [3, 1]}
    )

    county_map(county, axes[0])
    locator_map(county, axes[1])

    count = nc_counties.loc[
        nc_counties["NAME"] == county,
        "landfill_count"
    ].iloc[0]

    fig.suptitle(
        f"{county} County Landfill Atlas",
        fontsize=18,
        fontweight="bold"
    )

    fig.text(
        0.5, 0.03,
        f"{county} County has {count} landfills.",
        ha="center",
        fontsize=14
    )

    plt.tight_layout(rect=[0, 0.07, 1, 0.93])

    pdf.savefig(fig)

    plt.close(fig)


with PdfPages("nc_landfill_atlas.pdf") as pdf:

    for county in nc_counties["NAME"]:
        county_figure(county, pdf)

print("Atlas created successfully!")

