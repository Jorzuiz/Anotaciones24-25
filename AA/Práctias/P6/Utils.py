from skl2onnx import to_onnx
from onnx2json import convert
import pickle
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def ExportONNX_JSON_TO_Custom(onnx_json,mlp):
    graphDic = onnx_json["graph"]
    initializer = graphDic["initializer"]
    s= "num_layers:"+str(mlp.n_layers_)+"\n"
    index = 0
    parameterIndex = 0
    for parameter in initializer:
        s += "parameter:"+str(parameterIndex)+"\n"
        print(parameter["dims"])
        s += "dims:"+str(parameter["dims"])+"\n"
        print(parameter["name"])
        s += "name:"+str(parameter["name"])+"\n"
        print(parameter["doubleData"])
        s += "values:"+str(parameter["doubleData"])+"\n"
        index = index + 1
        parameterIndex = index // 2
    return s

def ExportAllformatsMLPSKlearn(mlp,X,picklefileName,onixFileName,jsonFileName,customFileName):
    with open(picklefileName,'wb') as f:
        pickle.dump(mlp,f)
    
    onx = to_onnx(mlp, X[:1])
    with open(onixFileName, "wb") as f:
        f.write(onx.SerializeToString())
    
    onnx_json = convert(input_onnx_file_path=onixFileName,output_json_path=jsonFileName,json_indent=2)
    
    customFormat = ExportONNX_JSON_TO_Custom(onnx_json,mlp)
    with open(customFileName, 'w') as f:
        f.write(customFormat)
        
def export_to_json(model, filename):
    model_dict = {"num_layers": len(model.coefs_)}
    parameters = []

    for i, (coef, intercept) in enumerate(zip(model.coefs_, model.intercepts_)):
        parameter = {
            "parameter": i,
            "coefficient": {
                "dims": list(coef.shape),
                "values": coef.flatten().tolist()
            },
            "intercepts": {
                "dims": [1, len(intercept)],
                "values": intercept.tolist()
            }
        }
        parameters.append(parameter)

    model_dict["parameters"] = parameters

    with open(filename, 'w') as f:
        json.dump(model_dict, f)
def export_to_txt(model, filename):
    with open(filename, 'w') as f:
        num_layers = len(model.coefs_) + 1
        f.write(f"num_layers:{num_layers}\n")

        parameter_num = 0
        for _, (coefs, intercepts) in enumerate(zip(model.coefs_, model.intercepts_)):

            for param_type, param_values in [('coefficient', coefs), ('intercepts', intercepts)]:
                dims = list(map(str, reversed(param_values.shape)))
                f.write(f"parameter:{parameter_num}\n")
                f.write(f"dims:{dims}\n")
                f.write(f"name:{param_type}\n")
                f.write(f"values:{param_values.flatten().tolist()}\n")
            parameter_num += 1


#################################################################################
# Utils mios propios que pongo aqui como si fuese la parte de atrás de una nevera
#################################################################################

def load_traces(path):


    data = pd.read_csv('Data/SensoresSeparados/combined_file.csv')

    ray1 = data['ray1'].to_numpy()
    ray2 = data['ray2'].to_numpy()
    ray3 = data['ray3'].to_numpy()
    ray4 = data['ray4'].to_numpy()
    ray5 = data['ray5'].to_numpy()
    kartx = data['kartx'].to_numpy()
    kartz = data['kartz'].to_numpy()
    time = data['time'].to_numpy()

    X = np.array([ray1,ray2,ray3,ray4,ray5,kartx,kartz,time])
    X = X.T
    y = data['action']

    return data, X, y

def heatmap(data):

    plt.figure(figsize=(8, 8))

    action_colors = {
        'NONE': 'gray',
        'ACCELERATE': 'green',
        'BRAKE': 'red',
        'LEFT_ACCELERATE': 'blue',
        'RIGHT_ACCELERATE': 'orange',
        'LEFT_BRAKE': 'purple',
        'RIGHT_BRAKE': 'brown'
    }

    for action, color in action_colors.items():
        action_df = data[data['action'] == action]
        plt.scatter(action_df['kartx'], action_df['kartz'], marker='o', linestyle='-', color=color, label=action, s=5)

    # Esto nos generará un "mapa de calor" usando las posiciones del kart para ver que acciones se tomaron
    plt.xlabel('Posicion X')
    plt.ylabel('Posicion Z')
    plt.title('Trayectoria del Kart con acciones coloreadas')
    plt.legend(loc='best')
    plt.grid(True)
    plt.axis('equal')
    plt.show()

def frecuencias(data):
    action_counts = data['action'].value_counts() #Cuenta las veces que aparece cada accion
    plt.figure(figsize=(10, 6))
    
    plt.bar(action_counts.index, action_counts.values)
    plt.xlabel('Acción')
    plt.ylabel('Número de sucesos')
    plt.title('Distribución de las Acciones')
    #plt.xticks(rotation=45, ha='right') # Rotar las etiquetas
    plt.tight_layout()
    plt.show()

def sensores(data):
    plt.figure(figsize=(12, 6))  # Ajustar el tamaño de la figura para mejor visualización

    ray_colors = ['blue', 'orange', 'green', 'red', 'purple'] #Colores para cada rayo
    ray_labels = ['Ray 1', 'Ray 2', 'Ray 3', 'Ray 4', 'Ray 5']

    for i in range(1, 6):
        plt.scatter(data['time'], data[f'ray{i}'], label=ray_labels[i-1], color=ray_colors[i-1], s=5)

    plt.xlabel('Tiempo')
    plt.ylabel('Distancia del Rayo')
    plt.title('Distancia de los Rayos a lo largo del Tiempo')
    plt.legend()  # Mostrar la leyenda para identificar cada rayo
    plt.grid(True)  # Añadir una cuadrícula para facilitar la lectura
    plt.tight_layout()
    plt.show()

def sensores3D(salidaPCA, data):
    # import matplotlib
    # matplotlib.use('Qt5Agg')
    
    # Esta brujería hace que se pueda ver en 3d supeustamente, 
    # mi patata no lo tira y tristemente no me dará tiempo a hacerlo con la torre antes de entregar :(
    # matplotlib.use('TkAgg')

    principalDf = pd.DataFrame(data=salidaPCA, columns=['principal component 1', 'principal component 2', 'principal component 3'])
    visuales = pd.concat([principalDf, data['action']], axis=1)
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    #Colorear por accion
    actions = ['NONE', 'ACCELERATE', 'BRAKE', 'LEFT_ACCELERATE', 'RIGHT_ACCELERATE', 'LEFT_BRAKE', 'RIGHT_BRAKE']
    targets = actions
    colors = ['r', 'g', 'b', 'c', 'm', 'y', 'k']
    for target, color in zip(targets,colors):
        indicesToKeep = visuales['action'] == target
        ax.scatter(visuales.loc[indicesToKeep, 'principal component 1']
                , visuales.loc[indicesToKeep, 'principal component 2']
                , visuales.loc[indicesToKeep, 'principal component 3']
                , c = color
                , s = 10, label = target)
    ax.set_xlabel('Componente Principal 1', fontsize = 15)
    ax.set_ylabel('Componente Principal 2', fontsize = 15)
    ax.set_zlabel('Componente Principal 3', fontsize = 15)
    ax.set_title('PCA con 3 Componentes', fontsize = 20)
    ax.legend()
    ax.grid()
    plt.show()