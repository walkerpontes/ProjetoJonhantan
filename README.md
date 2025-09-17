Python 3.11 é necessario pq o pyaudio so funciona em versoes abaixo dessa

pip install SpeechRecognition 

pip install pyaudio



----------------------------------------------------------------------------------


Para as configuracoes do mic, tu precisa escolher qual sera usado no proprio windows
a biblioteca pyaudio, nao consegue acessar as informacoes. 

No celular:
baixe o WO Mic, o aplicativo responsavel por transformar o celular em mic
vai nos tres traços -> settings -> transport e muda para o bluetooth
volta e aperta o play pra startar a conexao

no PC: 
tu baixa o WO mic client: https://wolicheng.com/womic/download.html
instala os drivers e reinicia o pc
dentro do software, vai na aba connection-> connect...-> bluetooth e conecta com o celular
se nao aparecer, parea manualmente pelo windows, verifica se apareceu no wo, seleciona 
e dps aperta em connect
verifique no windows se ta usando o wo mic como mic principal de entrada
depois disso ta feito, teu celular virou um mic



depois testa o codigo pra ve se o reconhecimento ta funcionando

