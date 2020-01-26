
import os
class Aqraa:
    def read(self,filetype="image",path=os.getcwd()):
        self.filetype = filetype
        os.chdir(path)
        self.filesarray = []
        if self.filetype in ['image','photo','picture']:
            
            from scipy import misc
            for index,image in enumerate(os.listdir()):
                try:
                    self.filesarray.append(misc.imread(image))
                except:
                    print('is not photo ',image)
        if self.filetype in ['sound','voice','wav','mp3']:
            from scipy.io import wavfile
            
            for index,wav in enumerate(os.listdir()):
                try:
                    self.filesarray.append(wavfile.read(wav))
                except:
                    print(wav,'is not a sound')
        return self.filesarray


    def display(self,index=0):
        import matplotlib.pyplot as plt

        if self.filetype == 'image':
            plt.imshow(self.filesarray[index])
        else:
            print('len : ',range(len(self.filesarray[index][1])))
            plt.plot(self.filesarray[index][1])
        
        plt.show()
                
            
        

