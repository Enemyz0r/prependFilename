import glob, os


def rename(dir, pattern, titlePattern):
    k = 1
    for pathAndFilename in glob.iglob(os.path.join(dir, pattern)):
        title, ext = os.path.splitext(os.path.basename(pathAndFilename))
        a = (str(k)+'. ') + title
        os.rename(pathAndFilename, os.path.join(dir, titlePattern % a + ext))
        k += 1
