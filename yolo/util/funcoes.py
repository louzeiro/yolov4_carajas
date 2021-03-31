#funções auxiliares

import cv2 #openCV
import matplotlib.pyplot as plt

def exibir (diretorio):
  imagem = cv2.imread(diretorio)
  fig = plt.gcf() #
  fig.set_size_inches(18,18) # set o tamanho imagem
  plt.axis('off') # desabilitando a exibiçãão dos eixo
  plt.imshow(cv2.cvtColor(imagem,cv2.COLOR_BGR2RGB)) # convertendo
  plt.show() 

def detectar(imagem):
  #caminhoImagem = imagem
  pastaImg = '/content/yolov4_carajas/darknet/imagens'
  caminhoImagem = os.path.sep.join([pastaImg,imagem])  
  os.chdir("/content/yolov4_carajas/darknet/")

  os.system("./darknet detector test data/obj.data cfg/yolov4_drone.cfg yolov4_drone_best.weights {}".format(caminhoImagem))
  exibir("predictions.jpg")
  os.rename("predictions.jpg", 'results/resultado_{}'.format(imagem)) #salvando a predição na pasta results
