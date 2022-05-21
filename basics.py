#%%
import altair as alt
import plotnine as p9
import pandas as pd
# %%
mtcars = pd.read_csv('mtcars.csv')
mtcars
# %%
(alt.Chart(data=mtcars)
    .mark_point()
    .encode(x='wt',y='mpg',color='gear:N')
    )
# %%
(p9.ggplot(mtcars, p9.aes(x='wt',y='mpg',color='factor(gear)'))
    + p9.geom_point()
)
# %% Notes
# - p9 feels abit more verbose
# - p9 crops image unto data points, y axis starts at 10
# - p9 can save easily in Vscode's jupyter extension but output looks rasterized
# - altair ... options don't work

