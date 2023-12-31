## Installation

### Simulator
To install the simulator itself, you only need to go to the following link:
> https://www.coppeliarobotics.com/downloads

There, download the Edu version.
Once you have downloaded the installer, just click over it and follow the Wizard, it is recommended to just follow the default settings of the wizard and just click on yes.

### Python Client
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

### Java Client
> First, to use the the Java client, you first need to settle the Python client. The Java client relies on a wrapper of the Python client, that is why it is necessary. First make sure that the the Python client is working before using the Java client.

For Java, you also need to install the VecMath library, which is used to calculate the Euler Angles.

To use the vecmath library from the refactured version of jogamp in your project, you'll need to manually download the jar file and add it as a local dependency. Right-click on the project's dependencies in NetBeans IDE and add the following dependency:

```
group id: org.jogamp.java3d
artifact id: vecmath
type: jar
```
If the dependency already exists, right-click on it and manually add the needed jar file.

To see an example of how to add a JAR file manually, you can check minute 5:16 of this [video](https://www.youtube.com/watch?v=L5fRigcRqGY&t=465s). 

## How to use it

This relies on the CoppeliaSim Regular API. You can find information (only for Lua and Python) on all the methods it has on: [CoppeliaSim User Manual](https://www.coppeliarobotics.com/helpFiles/). At the left menu in:
* Writing code -> CoppeliaSim API framework -> Regular API reference

You always have to start your program with the following lines of code:
``` python
from coppesim_zmqremoteapi_client import RemoteAPIClient

# Starts the CoppeliaSim client
client = RemoteAPIClient()
sim = client.require('sim')

# Run a simulation in stepping mode:
sim.setStepping(True)
sim.startSimulation()
```


Since we are running in stepping mode, after every single operation performed in the simulation, you should follow with
``` python
client.step()  # triggers next simulation step
```

And you should always end your program with these lines of code:
``` python
sim.stopSimulation()
```

## What is the stepping mode
In this mode, the simulation waits before advancing to the next simulation step. This trigger can be sent by the client using the remote. This mode gives the client more control over the simulation, as they can decide when to advance the simulation time. This feature is useful for debugging and testing purposes.

# CoppeliaSim documentation and support

## Do not confuse
There is a deprecated library that uses methods starting with simx. Notice that the methods of the regularAPI use methods starting with, sim (without x), not simx.

Sadly, by October of 2023, the only existing documentation for the new sim methods are the [RegularAPI Reference](https://www.coppeliarobotics.com/helpFiles/) and the examples in the [python clients in the GitHub repository](https://github.com/CoppeliaRobotics/zmqRemoteApi/tree/master/clients/python).

All the forums, YouTube videos and AI chatbots give information about simx (which is legacy code, so using it is not the best practice and it is not the library used in this project). 

Unless you want to use simx examples as a secondary support for understanding, it is highly recommended to just focus on the Regular API Reference to avoid losing time with no point. 

## Other support
To get support from the CoppeliaSim vendors or other users, you can use the official [forum](https://forum.coppeliarobotics.com/). To post something you need an account (you can use a Google account too). There you can ask questions or report bugs and sometimes they answer.

# Problems of CoppeliaSim to consider
CoppeliaSim can be difficult to learn and use. The interface can be confusing, and the documentation is not always helpful. As said before, the material is very limited and the support to developers is very little.

Moreover, the simulator is not always stable. Sometimes, simulations can crash or become unstable.
In addition, they are constatly realising new updates. But this is many times a problems. Because they new updates tend to be unstable. So commonly they produce errors or come with bugs. This forces the developer to wait for another release hoping it is stable. Or rollback to a previous version, but in the forum and the user manual, they only give support for the latest version. So with a rollback you lose receiving support. In addition, sometimes with new updates they change the name of methods, so you have to rewrite your code. Also, the few code examples they release change drastically very frequently. So it is difficult ot keep a track on how to work with this tool.

Another problem, is that they are focusing heavily just in Python and Lua. Which is leaving a detrimental support for other languages. As said before, they are wrapping everything to Python. Which adds overhead by always needing all the setup for the Python client, also reduces the performance and affects a complete compatibility with other languages.

CoppeliaSim is not always easy to customize. The functions of the API, primitive shapes and other aspects are very limited and does not leave to much room for customization or making certain actions in the simulator. The simulator's API is not very well documented, and it can be difficult to modify the simulator's behavior. Many times it is not clear what a function does or what ypu should send as parameters.
