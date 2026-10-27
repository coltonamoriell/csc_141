import plotly.express as px
from die import Die

die_1 = Die()
die_2 = Die()

# Generate rolls using a comprehension
results = [die_1.roll() + die_2.roll() for _ in range(1_000)]

max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result + 1)

# Generate frequencies using a list comprehension
frequencies = [results.count(value) for value in poss_results]

title = "Results of Rolling Two D6 Dice (Using Comprehensions)"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.update_layout(xaxis_dtick=1)
fig.show()