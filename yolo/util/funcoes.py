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
  
def arquivosConf():
## Copiando os arquivos de configuração
  os.system('cp ../yolo/confs/obj.names data/')
  os.system('cp ../yolo/confs/obj.data data/')
  os.system('cp ../yolo/confs/yolov4_drone.cfg cfg/')
  
  print('Carregando os pesos para o ambiente'...)
  os.system('wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate "https://docs.google.com/uc?export=download&id=17K3pgrjxjkUdCJfwpbTMTMQx8ObEzA9q" -O- | sed -rn "s/.*confirm=([0-9A-Za-z_]+).*/\1\n/p")&id=17K3pgrjxjkUdCJfwpbTMTMQx8ObEzA9q" -O yolov4_drone_best.weights && rm -rf /tmp/cookies.txt')
  print('Pesos carregados')

