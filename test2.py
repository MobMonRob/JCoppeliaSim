import time

from coppeliasim_zmqremoteapi_client import RemoteAPIClient

def func(input1, input2):
    print('Hello', input1, input2)
    return 21

print('Program started')

client = RemoteAPIClient()
sim = client.require('sim')

# Create a few dummies and set their positions:
handles = [sim.createDummy(0.01, 12 * [0]) for _ in range(50)]
for i, h in enumerate(handles):
    sim.setObjectPosition(h, -1, [0.01 * i, 0.01 * i, 0.01 * i])

# Run a simulation in asynchronous mode:
sim.startSimulation()
while (t := sim.getSimulationTime()) < 3:
    s = f'Simulation time: {t:.2f} [s] (simulation running asynchronously '\
        'to client, i.e. non-stepping)'
    print(s)
    sim.addLog(sim.verbosity_scriptinfos, s)
    # sim.testCB(21,func,42) # see below
sim.stopSimulation()
# If you need to make sure we really stopped:
while sim.getSimulationState() != sim.simulation_stopped:
    time.sleep(0.1)

# Run a simulation in stepping mode:
sim.setStepping(True)
sim.startSimulation()
while (t := sim.getSimulationTime()) < 3:
    s = f'Simulation time: {t:.2f} [s] (simulation running synchronously '\
        'to client, i.e. stepping)'
    print(s)
    sim.addLog(sim.verbosity_scriptinfos, s)
    sim.step()  # triggers next simulation step
sim.stopSimulation()

# Remove the dummies created earlier:
for h in handles:
    sim.removeObject(h)

print('Program ended')