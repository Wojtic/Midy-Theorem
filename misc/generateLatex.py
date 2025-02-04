from main import checkMidyProperty, real

f = open("output.tex", "w")
f.write("\\documentclass[fleqn]{article}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n")
f.write("\\usepackage[left=1.5cm, right=1.5cm]{geometry}\n")
f.write("\\begin{document}\n")


for j in range(1, 10):
    print(j)
    f.write("$\\boldsymbol{\\beta^2 = " + str(j) + "\\beta + 1}$\n")

    beta = real(1, 1, j, 1, 0)
    for i in range(1, 100):
        if i % 10 == 0:
            print(i)
        output = checkMidyProperty(beta, i)
        if output:
            expansion = "".join(map(lambda x: str(x), output[2]))
            f.write("\\begin{equation*}\n\\begin{split}\n")
            f.write("(\\frac{" + str(output[1]) + "}{" + str(i) + "})_\\beta = 0." + expansion + "^\omega\n")
            f.write("\\end{split}\\end{equation*}\n")


f.write("\\end{document}")
f.close()
