import plotly.graph_objects as gp


def PopulationPyramid(data, name):
    y_age = data['Age']
    x_M = data['M']
    x_F = data['F'] * -1

    # Creating instance of the figure
    fig = gp.Figure()

    # Adding Male data to the figure
    fig.add_trace(gp.Bar(y=y_age, x=x_M,
                         name='Male',
                         orientation='h'))

    # Adding Female data to the figure
    fig.add_trace(gp.Bar(y=y_age, x=x_F,
                         name='Female', orientation='h'))

    # Updating the layout for our graph
    fig.update_layout(title=f'Population Pyramid of {name}',
                      title_font_size=22, barmode='relative',
                      bargap=0.0, bargroupgap=0,
                      xaxis=dict(tickvals=[-60000000, -40000000, -20000000,
                                           0, 20000000, 40000000, 60000000],

                                 ticktext=['6M', '4M', '2M', '0',
                                           '2M', '4M', '6M'],

                                 title='Population in Millions',
                                 title_font_size=14)
                      )

    fig.show()
