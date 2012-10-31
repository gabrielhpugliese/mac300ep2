Gabriel Henrique Pugliese - 5639061
EP2 - MAC300

1) Requerimentos:

Precisei instalar o PIL e o numpy/scipy com os seguintes passos (Ubuntu):

sudo apt-get install libjpeg8 libjpeg62-dev libfreetype6 libfreetype6-dev
sudo ln -s /usr/lib/x86_64-linux-gnu/libjpeg.so /usr/lib
sudo ln -s /usr/lib/x86_64-linux-gnu/libfreetype.so /usr/lib
sudo ln -s /usr/lib/x86_64-linux-gnu/libz.so /usr/lib
sudo pip install -U PIL numpy scipy argparse matplotlib

2) Para rodar o programa:

python main.py --metodo foto.jpg
Exemplo:
python main.py --blur Lena.jpg

3) Pastas

Existe uma pasta com as fotos originais e transformadas e outra para o relatorio.
