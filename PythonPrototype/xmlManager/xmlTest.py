"""
This class is deals with opening the path XML file
This uses the SAX library, which offers several advantages
First, it is also available for Java, so this code can be easily migrated
In addition, this library is a better option for large XML files
Because it does not load the whole file in RAM
but instead it works by events, making it significantly lighter weight
IMPORTANT: THIS CODE HAS NOT BEEN TESTED
Take this just as a prototype
"""
import xml.sax
import coppeliaClasses.euclidViewerCoppelia

class PlannerCommandHandler(xml.sax.ContentHandler):
    
    """
    @dev: constructor
    @param: None
    @returns: None
    """
    def __init__(self):
        # Current element is very important because determines the what is being read in that moment
        self.current_element = ""
        self.path_data = {}
        self.euclidViewerCoppelia = coppeliaClasses.euclidViewerCoppelia.EuclidViewerCoppelia()

    """
    @dev: This function is excecuted when a new element (tag) is read in the XML file
    @param: name: String with the name of the element read at the moment
            attrs: iterable with the attributes of the current element
    @returns: None
    @author: Andres Masis
    """
    def startElement(self, name, attrs):
        # Updates the value of current element to tell what is going on
        self.current_element = name
        if name == "path":
            # Tells what we find inside a path, in this case positionType, orientationType and points
            self.path_data = {
                "positionType": None,
                "orientationType": None,
                "points": []
            }
 
    """
    @dev: This function is excecuted when a element (tag) finishes (reaches the closing tab)
    @param: name: String with the name of the element read at the moment
    @returns: None
    @author: Andres Masis
    """
    def endElement(self, name):
        if name == "path":
            # Prints what has been read in the element
            print("Path Data:", self.path_data)

    """
    @dev: This function is excecuted every time a character is read
    @param: name: String with the name of the element read at the moment
    @returns: None
    @author: Andres Masis
    """
    def characters(self, content):
        # Gets the content of the current read data
        content = content.strip()

        # If there is nothing, it stops the functiom
        if not content:
            return
        
        # Checks if the current element is positionType
        if self.current_element == "positionType":
            self.path_data["positionType"] = int(content)

        # Checks if the current element is orientationType
        elif self.current_element == "orientationType":
            self.path_data["orientationType"] = int(content)

        # Checks if the current element is point
        elif self.current_element == "point":
            # A point is a complex data type, so it has to be split in its different parts
            pose_data = content.split()

            # Creates a dictionary (hash map) with the position and orientation
            pose_opt = {
                "position": (float(pose_data[0]), float(pose_data[1]), float(pose_data[2])),
                "orientation": (float(pose_data[3]), float(pose_data[4]), float(pose_data[5]), float(pose_data[6]))
            }
            # Gets the pathParameterOpt
            path_parameter_opt = int(pose_data[7])
            
            self.path_data["points"].append({"poseOpt": pose_opt, "pathParameterOpt": path_parameter_opt})

            # Generates the given Coppelia visualization
            location = (float(pose_data[0]), float(pose_data[1]), float(pose_data[2]))
            radius = 0.05
            color = (255, 0, 0)
            label = "point"
            transparency = False
            # For this specific case, the orientation is not important, because we are adding a sphere
            self.euclidViewerCoppelia.addSphere(location, radius, color, label, transparency)


 

# Create a SAX parser and parse the XML file
xml_file_path = "your_xml_file.xml"  # Replace with the actual path to your XML file
parser = xml.sax.make_parser()
handler = PlannerCommandHandler()
parser.setContentHandler(handler)
parser.parse(xml_file_path)

def parse_collision_objects(self, xml_path, myHandler):
    handler = myHandler
    parser = xml.sax.make_parser()
    parser.setContentHandler(handler)
    parser.parse(open(xml_path))

    return handler.collisionObjects
