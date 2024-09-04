import re
mesh = open("mesh.su2","w")
def mesh_writeout(mesh_definition):
    count_face3 = 0
    count_face4 = 0
    for face in mesh_definition:
        if face[0] == '3':
            count_face3+=1
        else:
            count_face4+=1
    if count_face3 == 4:
        tetra(mesh_definition)
    elif count_face3 == 2:
        prism(mesh_definition)
    elif count_face4 == 6:
        hexa(mesh_definition)

def tetra(mesh_definition):
    face_1 = mesh_definition[0][1][1:-1].split()
    face_2 = mesh_definition[1][1][1:-1].split()
    for coord in face_2:
        if coord in face_1:
            continue
        else:
            break
    mesh.write("10")
    mesh.write("\t")
    mesh.write(face_1[0])
    mesh.write("\t")
    mesh.write(face_1[1])
    mesh.write("\t")
    mesh.write(face_1[2])
    mesh.write("\t")
    mesh.write(coord)
    mesh.write("\n")
def prism(mesh_definition):
    order_face = []
    firstOccurence = 0
    for face in mesh_definition:
        order_face.append(face[1][1:-1].split())
    for orderFace in order_face:
        if len(orderFace) == 3:
            if firstOccurence == 0:
                x,y,z = orderFace
                firstOccurence = 1
    for orderFace in order_face:
        got_friend_of_x=0
        got_friend_of_y=0
        got_friend_of_z=0
        if len(orderFace) == 4:
            if (x in orderFace) & (got_friend_of_x == 0):
                index_x = orderFace.index(x)
                friend1_of_x = orderFace[index_x-1]
                if index_x==3:
                    friend2_of_x = orderFace[0]
                else:
                    friend2_of_x = orderFace[index_x+1]
                if (friend1_of_x == y) | (friend1_of_x == z):
                    true_friend_of_x = friend2_of_x
                else:
                    true_friend_of_x = friend1_of_x
                got_friend_of_x=1
            if (y in orderFace) & (got_friend_of_y == 0):
                index_y = orderFace.index(y)
                friend1_of_y = orderFace[index_y-1]
                if index_y==3:
                    friend2_of_y = orderFace[0]
                else:
                    friend2_of_y = orderFace[index_y+1]
                if (friend1_of_y == x) | (friend1_of_y == z):
                    true_friend_of_y = friend2_of_y
                else:
                    true_friend_of_y = friend1_of_y
                got_friend_of_y=1
            if (z in orderFace) & (got_friend_of_z == 0):
                index_z = orderFace.index(z)
                friend1_of_z = orderFace[index_z-1]
                if index_z==3:
                    friend2_of_z = orderFace[0]
                else:
                    friend2_of_z = orderFace[index_z+1]
                if (friend1_of_z == x) | (friend1_of_z == y):
                    true_friend_of_z = friend2_of_z
                else:
                    true_friend_of_z = friend1_of_z
                got_friend_of_z = 1
    #print(x, y, z, true_friend_of_x,true_friend_of_y,true_friend_of_z)
    mesh.write("13")
    mesh.write("\t")
    mesh.write(x)
    mesh.write("\t")
    mesh.write(y)
    mesh.write("\t")
    mesh.write(z)
    mesh.write("\t")
    mesh.write(true_friend_of_x)
    mesh.write("\t")
    mesh.write(true_friend_of_y)
    mesh.write("\t")
    mesh.write(true_friend_of_z)
    mesh.write("\n")
def hexa(mesh_definition):
    order_face = []
    firstOccurence = 0
    for face in mesh_definition:
        order_face.append(face[1][1:-1].split())
    for orderFace in order_face:
        if len(orderFace) == 4: #i mean ko can check but yknow aint nothing called being too careful
            if firstOccurence == 0:
                a,b,c,d = orderFace
                firstOccurence = 1
    for orderFace in order_face:
        got_friend_of_a=0
        got_friend_of_b=0
        got_friend_of_c=0
        got_friend_of_d=0
        if len(orderFace) == 4:
            if (a in orderFace) & (got_friend_of_a == 0):
                index_a = orderFace.index(a)
                friend1_of_a = orderFace[index_a-1]
                if index_a==3:
                    friend2_of_a = orderFace[0]
                else:
                    friend2_of_a = orderFace[index_a+1]
                if (friend1_of_a == b) | (friend1_of_a == d):
                    true_friend_of_a = friend2_of_a
                else:
                    true_friend_of_a = friend1_of_a
                got_friend_of_a=1
            if (b in orderFace) & (got_friend_of_b == 0):
                index_b = orderFace.index(b)
                friend1_of_b = orderFace[index_b-1]
                if index_b==3:
                    friend2_of_b = orderFace[0]
                else:
                    friend2_of_b = orderFace[index_b+1]
                if (friend1_of_b == a) | (friend1_of_b == c):
                    true_friend_of_b = friend2_of_b
                else:
                    true_friend_of_b = friend1_of_b
                got_friend_of_b=1
            if (c in orderFace) & (got_friend_of_c == 0):
                index_c = orderFace.index(c)
                friend1_of_c = orderFace[index_c-1]
                if index_c==3:
                    friend2_of_c = orderFace[0]
                else:
                    friend2_of_c = orderFace[index_c+1]
                if (friend1_of_c == b) | (friend1_of_c == d):
                    true_friend_of_c = friend2_of_c
                else:
                    true_friend_of_c = friend1_of_c
                got_friend_of_c=1
            if (d in orderFace) & (got_friend_of_d == 0):
                index_d = orderFace.index(d)
                friend1_of_d = orderFace[index_d-1]
                if index_d==3:
                    friend2_of_d = orderFace[0]
                else:
                    friend2_of_d = orderFace[index_d+1]
                if (friend1_of_d == a) | (friend1_of_d == b):
                    true_friend_of_d = friend2_of_d
                else:
                    true_friend_of_d = friend1_of_d
                got_friend_of_d=1
    mesh.write("12")
    mesh.write("\t")
    mesh.write(a)
    mesh.write("\t")
    mesh.write(b)
    mesh.write("\t")
    mesh.write(c)
    mesh.write("\t")
    mesh.write(d)
    mesh.write("\t")
    mesh.write(true_friend_of_a)
    mesh.write("\t")
    mesh.write(true_friend_of_b)
    mesh.write("\t")
    mesh.write(true_friend_of_c)
    mesh.write("\t")
    mesh.write(true_friend_of_d)
    mesh.write("\n")

startRead = 0
faces = open("faces", "r")
faceList = []
for line in faces:
    if "object" in line:
        startRead = 1
    if startRead == 1:
        face_def_3 = re.findall(r"(3)(\(\d{1,15} \d{1,15} \d{1,15}\))",line);
        face_def_4 = re.findall(r"(4)(\(\d{1,15} \d{1,15} \d{1,15} \d{1,15}\))",line);
        if len(face_def_3) != 0:
            faceList.append(face_def_3[0]) #phan tu 0 la list [3, (1 2 3)]
        if len(face_def_4) != 0:
            faceList.append(face_def_4[0])
faces.close()

owner = open("owner","r")
ownerList = []
startNELEM = 0
startRead = 0
for line in owner:
    if "object" in line:
        startRead = 1
    if startRead == 1:
        nelem = re.findall(r"\d{1,15}", line)
        if len(nelem) != 0:
            if startNELEM == 0: 
                nFaces = nelem[0]
                startNELEM = 1
            else:
                ownerList.append(int(nelem[0]))
owner.close()

startRead = 0
neighbour = open("neighbour","r")
neighbourList = []
startNeighbour = 0
for line in neighbour:
    if "object" in line:
        startRead = 1
    if startRead == 1:
        nelem = re.findall(r"\d{1,15}", line)
        if len(nelem) != 0:
            if startNeighbour == 0: 
                #nFaces = nelem[0]
                startNeighbour = 1
            else:
                neighbourList.append(int(nelem[0]))
neighbour.close()
largestCell = max(ownerList) + 1 if max(ownerList) > max(neighbourList) else (max(neighbourList) + 1)

mesh.write("NDIME= 3")
mesh.write("\n")
mesh.write("NELEM= ")
mesh.write(str(largestCell))
mesh.write("\n")

cell_definition = []
for k in range(largestCell):
    cell_definition.append([])
for j in range(len(ownerList)):
    cell_definition[ownerList[j]].append(faceList[j])
for q in range(len(neighbourList)):
    cell_definition[neighbourList[q]].append(faceList[q])
for k in range(largestCell):
    mesh_writeout(cell_definition[k])
'''
for i in range(largestCell):
    cell_i_definition = []
    for j in range(len(ownerList)):
        if ownerList[j] == i:
            cell_definition.append(faceList[j])
    for k in range(len(neighbourList)):
        if neighbourList[k] == i:
            cell_definition.append(faceList[k])
    mesh_writeout(cell_definition)

'''
points = open("points","r")
had_npoin = 0
startRead = 0
for line in points:
    if "object" in line:
        startRead = 1
    if startRead == 1:
        npoin = re.findall(r"\d{1,15}",line)                    
        coord = re.findall(r"\d.\d{1,15}",line)
        if len(npoin) != 0:
           if had_npoin==0:
                mesh.write('NPOIN= ')
                mesh.write(npoin[0])
                mesh.write('\n')
                had_npoin = 1
                #print("NPOIN=", npoin, "\n")
           else:
                x,y,z = line[1:-2].split()
                mesh.write(x)
                mesh.write(" ")
                mesh.write(y)
                mesh.write(" ")
                mesh.write(z)
                mesh.write("\n")
points.close()

boundary = open("boundary","r")
startRead = 0
first_occurence = 0
startRead = 0
marker_tag = []
marker_nelems = []
marker_startFace = []
for line in boundary:
    if "object" in line:
        startRead = 1
    if startRead == 1:
        if "nFaces" in line:
            marker_nelems.append(line.split()[1][:-1])
        if "startFace" in line:
            marker_startFace.append(line.split()[1][:-1])
        if "{" in line:
            marker_tag.append(nameFace[4:-1])
        if len(line) != 0:
            nameFace = line
            
mesh.write("NMARK= ")
mesh.write(str(len(marker_tag)))
mesh.write("\n")
for q in range(len(marker_tag)):
    mesh.write("MAKER_TAG= ")
    mesh.write(marker_tag[q])
    mesh.write("\n")
    mesh.write("MARKER_ELEMS= ")
    mesh.write(marker_nelems[q])
    mesh.write("\n")
    for r in range(int(marker_nelems[q])):
        if faceList[int(marker_startFace[q])+r][0] == '4':
            mesh.write("9")
            mesh.write("\t")
            a,b,c,d = faceList[int(marker_startFace[q])+r][1][1:-1].split()
            mesh.write(a)
            mesh.write("\t")
            mesh.write(b)
            mesh.write("\t")
            mesh.write(c)
            mesh.write("\t")
            mesh.write(d)
            mesh.write("\n")
        else:
            mesh.write("5")
            mesh.write("\t")
            a,b,c = faceList[int(marker_startFace[q])+r][1][1:-1].split()
            mesh.write(a)
            mesh.write("\t")
            mesh.write(b)
            mesh.write("\t")
            mesh.write(c)
            mesh.write("\n")
boundary.close()