from pulp import LpProblem, LpVariable, LpMaximize, PULP_CBC_CMD

def solve_optimization(specs, params):
    prob = LpProblem("DemoOptimization", LpMaximize)

    panel = LpVariable(
        'panel_count',
        lowBound=specs['variables']['panel_count'][0],
        upBound=specs['variables']['panel_count'][1],
        cat='Integer'
    )
    battery = LpVariable(
        'battery_capacity',
        lowBound=specs['variables']['battery_capacity'][0],
        upBound=specs['variables']['battery_capacity'][1]
    )

    # Example linear objective
    prob += 5 * panel + 2 * battery

    # Budget constraint
    prob += 1000 * panel + 50 * battery <= specs['constraints']['budget']

    prob.solve(PULP_CBC_CMD(msg=False))

    return {
        'panel_count': panel.value(),
        'battery_capacity': battery.value(),
        'objective_value': prob.objective.value()
  }
