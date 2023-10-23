## Installation

### Simulator
To install the simulator itself, you only need to go to the following link:
> https://www.coppeliarobotics.com/downloads

There, download the Edu version.
Once you have downloaded the installer, just click over it and follow the Wizard, it is recommended to just follow the default settings of the wizard and just click on yes. i

### Python Library
In order for the Python library to work properly, it needs some previous requirements.
1. Make sure your Python interpreter is at least 3.8
```
python –version
```

2. Install xsltproc (recommended with [Chocolatey](https://chocolatey.org/install))

*Once you have installed choco, just run the following command:*
```
choco install xsltproc
```

3. Run the following commands:
```
$ python -m pip install xmlschema
$ python -m pip install pyzmq
$ python -m pip install cbor
```

*By this point your Python code should already be working, but if you are having problems, you may try to execute the following commands as a POSSIBLE solution*
```
$ git clone --recursive https://github.com/CoppeliaRobotics/zmqRemoteApi
$ cd zmqRemoteApi
$ git checkout coppeliasim-v4.5.0-rev0
$ mkdir -p build && cd build
$ cmake -DCMAKE_BUILD_TYPE=Release ..
$ cmake --build .
$ cmake --install .
```
-- If cmake is not recognized as a command [this video](https://www.youtube.com/watch?v=GJy_bw2Vg5c) can help: 

## How to use it

This relies on the CoppeliaSim Regular API. You can find information (only for C/C++, Lua and Python) on all the methods it has on: [CoppeliaSim User Manual](https://www.coppeliarobotics.com/helpFiles/). At the left menu in:
* Writing code -> CoppeliaSim API framework -> Regular API reference

You always have to start your program with the following lines of code:
``` python
from coppesim_zmqremoteapi_client import RemoteAPIClient

client = RemoteAPIClient()
sim = client.getObject('sim')

# Makes sure that the idle loop runs at full speed for this program:
defaultIdleFps = sim.getInt32Param(sim.intparam_idle_fps)
sim.setInt32Param(sim.intparam_idle_fps, 0)

# Run a simulation in stepping mode:
client.setStepping(True)
sim.startSimulation()
```


Since we are running in stepping mode, after every single operation performed in the simulation, you should follow with
``` python
client.step()  # triggers next simulation step
```

And you should always end your program with these lines of code:
``` python
sim.stopSimulation()

# Restore the original idle loop frequency, no step() needed here
sim.setInt32Param(sim.intparam_idle_fps, defaultIdleFps)
```

## What is the stepping mode
In this mode, the simulation waits before advancing to the next simulation step. This trigger can be sent by the client using the remote. This mode gives the client more control over the simulation, as they can decide when to advance the simulation time. This feature is useful for debugging and testing purposes.

## Do not confuse
There is a deprecated library that uses methods starting with simx. Notice that the methods of the regularAPI use methods starting with, sim (without x), not simx.

Sadly, by October of 2023, the only existing documentation for the new sim methods are the [RegularAPI Reference](https://www.coppeliarobotics.com/helpFiles/) and the examples in the [python clients in the GitHub repository](https://github.com/CoppeliaRobotics/zmqRemoteApi/tree/master/clients/python).

All the forums, YouTube videos and AI chatbots give information about simx (which is legacy code, so using it is not the best practice and it is not the library used in this project). 

Unless you want to use simx examples as a secondary support for understanding, it is highly recommended to just focus on the Regular API Reference to avoid losing time with no point. 
