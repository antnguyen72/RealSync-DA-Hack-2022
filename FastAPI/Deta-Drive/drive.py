#import Deta
from deta import Deta

# Initialize with a project key
deta = Deta("example_project_key123")

# Connect to or create a datanase
drive = deta.Drive("drive_name")

# Can create as many drives as you want
photos = deta.Drive("photos")