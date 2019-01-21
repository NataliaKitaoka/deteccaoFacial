#deteccaoFacial

Neste repositório está contido um script de detecção facial utilizando a biblioteca openCV em Python3.
O classificador facial utilizado foi o cascadeClassifier().Ele é um classificador pré-treinado que baseia-se em uma cascata de classificadores mais simples que são aplicados a regiões de interesse específicas (ROI), que no caso são as faces detectadas em uma imagem de entrada, dessas ROIs são extraídas as Haar-features necessárias para tomada da decisão de presença ou ausência do objeto de interesse.

*Pré-requisitos:
- instalação do python3;
- instalação do módulo openCV2;
- instalação do módulo Numpy;
- os arquivos .xml dos classificadores precisam estar no mesmo diretório do código.


