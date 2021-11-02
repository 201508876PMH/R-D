from matplotlib import pyplot as plt


class Utils:
    def __init__(self):
        pass
    
    
    def show_imgs(self, x_test, dimension, n=10):
        plt.figure(figsize=(20, 4))
        for i in range(n):
            ax = plt.subplot(2, n, i+1)
            plt.imshow(x_test[i].reshape(dimension,dimension))
            plt.gray()
            ax.get_xaxis().set_visible(False)
            ax.get_yaxis().set_visible(False)
        plt.show()