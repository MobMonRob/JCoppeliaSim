# CoppeliaSim Visualization
This project allows to visualize different elements in CoppeliaSim robotics simulator.
This project currently is written in Python, but it is intended to be converted to Java.
This project is closely related to an interfeace written by Dr. Oliver Rettig.
As a general description in this project you can visualize lines, spheres, load robots, generate .obj files and read data from XML.

If you have questions, you can contact:
email: andres.masis.rojas@gmail.com
WhatsApp: (+506) 6071 7600 

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

# Coniderations and Limitations

### CoppeliaSim Java Client not Working
Right now, the project only runs in Python because the CoppeliaSim client is not working. Even just clonning their code without any changes, it still fails.
Apparently, the error is produced because CoppeliaSim is trying to execute a command that does not exist in Windows. So probably to solve this, you can run the Java client from CoppeliaSim in a Linux machine (better if it is Ubuntu), but this is not for sure the solution. Another option, is to wait until Coppelia releases a stable version with this problem solved, but there is no certainty when this will happen. Besides, it seems that Coppelia is heavily focusing just in Python and Lua. Even, in their new documentation, the deleted all the examples for other languages, and just focused in Python and Lua. So this is concerning about the support for Java. 

In case the Java client cannot be fixed, it can also be possible to write a wrapper to use Python code in a Java project. So all the code of this project can be used in the porject of Dr. Oliver. Or, have a wrapper to use Java code in a Python project, in order to import Dr. Olver´s library in this project. However, this is a big tasks. In addition, the performance may be quite slow because both languages run in virtual machines, so this add too much overhead. If you choose to go for a Python/Java wrapper, please do not waste time in Jython. Jython is an extremely popular tool to combine Python and Java, and it is the leader for this purpose. Indeed it is a robust tool, the problem with it is that it is just for Python 2. And Coppelia´s client and this project are written in Python 3, so Jython will not work.

If you want to use a wrapper but you are concerned about the performance, C++ may be an option. Because CoppeliaSim also has a client for C++. However, I have not tried this C++ client, therefore I have no idea if it works properly or not. But hopefully it works, in this case the wrapper can be an option. But you still have to take into account the efforts of trying this C++ client, and it case it works, rewriting all this Python project into C++ and then writting a Java/C++ wrapper. In addition, as stated before, it seems that CoppeliaSim is decreasing the support to other programming languages, so this may be a disadvantage for C++.

So, the best option is to have a Java client working. Furthermore, because this project was always developed thinking about Java. So all the libraries used are also availabel for Java. So this should allow a seamless migration. Nevertheless, if Windows is not the problem, this is mostly outside of the scope of the lab and it is something that has to be done by the CoppeliaSim team.

### Euler angles
Another issue to consider is the Euler angles. CoppeliaSim manages the orientation of its objects with Euler angles. However, in this project there is nothing implemented to manage the Euler angles. However, Dr. Oliver has been working on this so maybe he has some interesting ideas about it.

### Curved line for angles
In additon, there are a couple of tasks that could not be completed on time. There is a small task of visualizing an angle as a "curved cylinder". This was started but could not be finished. For this, an .obj file is generated. So the curved is made of consecutive cuboids. You can visualize something similar [here](https://fab.cba.mit.edu/classes/863.12/people/pip/WK2/images/scored%20card%20exp%202_small.jpg). The whole idea has been plotted and some code was written.

The idea is to generate an .obj with of the "curved cylinder made of cuboids". To make this you create a partial circle. So, if ypu want 30 degrees, you generate 30 angles. If you want 150 degrees you generate 150 points, and so on. At this point we just have a simple curved line, we want something in 3d. Then we repeat the process of generating a partial circle, but now with a slightly bigger radius, to get a external circle. So, now we got thickness, it is not just a line. But it is still in 2d, we do not have height yet. Next, we take both lists, the one of the points of the inner circle and the one of the points of the outer circle and we clone them. To these clones, we change all their z points to 0.05. So they are mirroring the thick curved line but a bit upper. At this moment, we have just points but no shape yet. So we have to connect all the points using triangles. Once we have connected all the points we already have our curved line. The .obj file is ready. This is not fully implemented yet. Connecting the points with triangles is missing. In additon, the points are generated with a function from another case, so the list always come with an initial point of (0,0,0), For this, make sure to delete that (0,0,0).

We import this .obj as a model in the CoppeliaSim scene. Then we generate a small cone pointing horizontally. Then we give it the location and orientation of the last point of the curved line (CoppeliaSim does not know this so we have to save it in a variable from the previous steps). This will be the arrow. We merge both shapes into one. To the new shape, we set the appropiate color, position and orientation. Also we set a label, usually the value of the angle. For everyhthing described in this last paragraph, there is already code to do that, so you can reuse existing functions.

### XML file of path
This task has been implemented as a prototype but has not been tested yet. First the file is read with the SAX library (a library especially efficient for large files and also available for Java). This library reads single characters and detects when a tag is opened or closed. Depending on the element (point, positionType, orientationType) that SAX detects on the XML, we do a specific action in the simulation.

#### Fanuc CRX25 robot not available in CoppeliaSim
In addition, ideally for the XML file, the simulation has to be done with a Fanuc CRX25 robot. However, this robot does not come by default in CoppeliaSim, so it cannot be imported. Besides, in the internet there was not .ttm (CoppeliaSim files for robots) of the Fanuc CRX25, so there is the .ttm model of this robot at all.

It seems that the providers have an URDF model of this model. So an option will be to try to import the URDF file into the CoppeliaSim scene. Apparently, there is a module for that purpose, but it has not been tested in this project, so its efficiency cannot be tell. You can check the more [here](https://coppeliarobotics.com/helpFiles/en/importExport.htm).

In case the previous solution does not work, one can try to make the whole model on your own. However, this will be a lengthy process and there is a risk of not being very accurate to the real FANUC CRX25. You can find a very basic description on how to build your own .ttm files [here](https://www.youtube.com/watch?v=uoL4J9QDZK0)

As final resource, if none of the previous attempt worked, you can try to scale the simulation to the size of an UR10, which can be found as a .ttm file in CoppeliaSim. Nevertheless, the approah of rescaling will generate a lot of additional effort and it is prone to errors.

# Problems of CoppeliaSim to consider
CoppeliaSim can be difficult to learn and use. The interface can be confusing, and the documentation is not always helpful. As said before, the material is very limited and the support to developers is very little.

Moreover, the simulator is not always stable. Sometimes, simulations can crash or become unstable.
In addition, they are constatly realising new updates. But this is many times a problems. Because they new updates tend to be unstable. So commonly they produce errors or come with bugs. This forces the developer to wait for another release hoping it is stable. Or rollback to a previous version, but in the forum and the user manual, they only give support for the latest version. So with a rollback you lose receiving support. In addition, sometimes with new updates they change the name of methods, so you have to rewrite your code. Also, the few code examples they release change drastically very frequently. So it is difficult ot keep a track on how to work with this tool.

Another problem, is that they are focusing heavily just in Python and Lua. Which is leaving a detrimental support for other languages. As said before, they are wrapping everything to Python. Which adds overhead by always needing all the setup for the Python client, also reduces the performance and affects a complete compatibility with other languages.

CoppeliaSim is not always easy to customize. The functions of the API, primitive shapes and other aspects are very limited and does not leave to much room for customization or making certain actions in the simulator. The simulator's API is not very well documented, and it can be difficult to modify the simulator's behavior. Many times it is not clear what a function does or what ypu should send as parameters.
