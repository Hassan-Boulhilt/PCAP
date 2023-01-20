import sys 
# sys.path.append("./project_level1.tar.gz")
# print(sys.path)
                
# import project_level1.communication_level2.com as a
# import project_level1.cors_level2.utils as b
# import project_level1.cors_level2.additional_level3.security as c
# import project_level1.messaging_level2.event as e
# import project_level1.messaging_level2.queue as q
                
# #import folder from zipped folder
# import project_level1.tar.gz.communication_level2.com as a
# import project_level1.tar.gz.cors_level2.utils as b
# import project_level1.tar.gz.cors_level2.additional_level3.security as c
# import project_level1.tar.gz.messaging_level2.event as e
# import project_level1.tar.gz.messaging_level2.queue as q


# a.fun()
# b.fun()
# c.fun()
# e.fun()
# q.fun()
sys.path.append("packages.zip")

sys.path.append("project_level1.tar.gz")
print(sys.path)
# from zip package
from extra.iota import FunI
print(FunI())

# from tar.gz
from project_level1.cors_level2.com import utils
fun()