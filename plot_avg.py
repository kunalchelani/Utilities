import matplotlib.pyplot as plt
import numpy as np
import math as math

num_iteration_to_plot = 100
save_location = "/home/kunal/Plots/"
font_size_label = 30
font_size_tick = 25

inputfile = []
inputfile.append(open('/home/kunal/17may_recording/pos1/avg_values.txt', 'r'))
inputfile.append(open('/home/kunal/17may_recording/pos2/avg_values.txt', 'r'))
inputfile.append(open('/home/kunal/17may_recording/pos3/avg_values.txt', 'r'))
inputfile.append(open('/home/kunal/17may_recording/pos4/avg_values.txt', 'r'))

tableau20 = [(214, 39, 40),(44, 160, 44),(31, 119, 180)]

for i in range(len(tableau20)):    
    r, g, b = tableau20[i]    
    tableau20[i] = (r / 255., g / 255., b / 255.) 

def isRotationMatrix(R) :
    Rt = np.transpose(R)
    shouldBeIdentity = np.dot(Rt, R)
    I = np.identity(3, dtype = R.dtype)
    n = np.linalg.norm(I - shouldBeIdentity)
   # print n
    return n < 1e-3	

def rotationMatrixToEulerAngles(R) :
 
    assert(isRotationMatrix(R))
     
    sy = math.sqrt(R[0,0] * R[0,0] +  R[1,0] * R[1,0])
     
    singular = sy < 1e-6
 
    if  not singular :
        x = math.atan2(R[2,1] , R[2,2])
        y = math.atan2(-R[2,0], sy)
        z = math.atan2(R[1,0], R[0,0])
    else :
        x = math.atan2(-R[1,2], R[1,1])
        y = math.atan2(-R[2,0], sy)
        z = 0
 
    return np.array([x, y, z])


# File wise plotting starts here

graph_colors = ['r', 'g', 'b', 'k']

for i in range(0,len(inputfile)):

	iteration = []
	avg_rmse = []

	x_trans = []
	y_trans = []
	z_trans = []

	x_rot = []
	y_rot = []
	z_rot = []

	for k in range(1,num_iteration_to_plot):

		# Appending into iteration number and X, Y, Z translation 
		iteration.append(inputfile[i].readline().strip())
		x_trans.append(inputfile[i].readline().strip())
		y_trans.append(inputfile[i].readline().strip())
		z_trans.append(inputfile[i].readline().strip())
		
		# Rotation Matrice Issues 
		rot_row1 = map(float, inputfile[i].readline().strip().split())
		rot_row2 = map(float, inputfile[i].readline().strip().split())
		rot_row3 = map(float, inputfile[i].readline().strip().split())
		
		rotation_matrix = np.matrix([rot_row1, rot_row2, rot_row3])
		eulerAngles = rotationMatrixToEulerAngles(rotation_matrix)*57.32

		# Append individual rotations
		x_rot.append(eulerAngles[0])
		y_rot.append(eulerAngles[1])
		z_rot.append(eulerAngles[2])

		avg_rmse.append(inputfile[i].readline().strip())


	#plotting Values
	plt.figure(figsize = (20,10))
	ax = plt.subplot(111)
	ax.spines["top"].set_visible(False)  
	ax.spines["right"].set_visible(False)
	ax.plot(iteration, x_trans, color = tableau20[0], lw=2)
	plt.xlabel('Iteration number', fontsize = font_size_label)
	plt.ylabel('X (in m)', fontsize = font_size_label)
	plt.xticks(fontsize=font_size_tick)  
	plt.yticks(fontsize=font_size_tick)
	plot_title = "X_translation_dataset_"+str(i)+".png"
	plt.savefig(save_location+plot_title, bbox_inches="tight")



	plt.figure(figsize = (20,10))
	ax = plt.subplot(111)
	ax.spines["top"].set_visible(False)  
	ax.spines["right"].set_visible(False)	
	plt.plot(iteration, y_trans, color = tableau20[1], lw=2)
	plt.xlabel('Iteration number', fontsize = font_size_label)
	plt.ylabel('Y (in m)', fontsize = font_size_label)
	plt.xticks(fontsize=font_size_tick)  
	plt.yticks(fontsize=font_size_tick)	
	plot_title = "Y_translation_dataset_"+str(i)+".png"
	plt.savefig(save_location+plot_title, bbox_inches="tight")


	plt.figure(figsize = (20,10))
	ax = plt.subplot(111)
	ax.spines["top"].set_visible(False)  
	ax.spines["right"].set_visible(False)
	plt.plot(iteration, z_trans, color = tableau20[2], lw=2)
	plt.xlabel('Iteration number', fontsize = font_size_label)
	plt.ylabel('Z (in m)', fontsize = font_size_label)
	plt.xticks(fontsize=font_size_tick)  
	plt.yticks(fontsize=font_size_tick)
	plot_title = "Z_translation_dataset_"+str(i)+".png"
	plt.savefig(save_location+plot_title, bbox_inches="tight")




	# If rotations need to be plotetd



	# plt.plot(iteration, avg_rmse, 'k')
	# plt.xlabel('Iteration number')
	# plt.ylabel('Moving avg. RMSE')
	# plt.show()

	# plt.plot(iteration, x_rot, 'r')
	# plt.xlabel('Iteration number')
	# plt.ylabel('Moving avg. X-axis rotation')
	# plt.show()

	# plt.plot(iteration, y_rot, 'g')
	# plt.xlabel('Iteration number')
	# plt.ylabel('Moving avg. Y-axis rotation')
	# plt.show()

	# plt.plot(iteration, z_rot, 'b')
	# plt.xlabel('Iteration number')
	# plt.ylabel('Moving avg. Z-axis rotation')
	# plt.show()
