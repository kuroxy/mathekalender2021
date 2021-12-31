import imageio

filenames = [f"opdr13/World_{i}.png" for i in range(2000)]

images = []
for filename in filenames:
    images.append(imageio.imread(filename))
imageio.mimsave('world2000.gif', images)