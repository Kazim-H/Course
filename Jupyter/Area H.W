{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "59b7e631",
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "a = \"i have a square with length of one side is 10 cm and a rectangle with length = 7.5 cm and width = 9 cm also calculate the area and circumference of a circle with radius of 2.5 cm\"\n",
    "shape1=a[9:15]\n",
    "shape2=a[55:64]\n",
    "shape3=a[150:156]\n",
    "b =a[42:45] #Square Extraction\n",
    "c =a[79:82] #Rectangle length Extraction\n",
    "d =a[98:99] #Rectangle Width Extraction\n",
    "e =a[172:175] #Circle Radius Extraction\n",
    "ls = int(b)\n",
    "lr = float(c)\n",
    "lw = int(d)\n",
    "cr = float(e)\n",
    "print(\"---------Area of\",shape1, \"---------\")\n",
    "print(\"Length= \",ls, \"cm\")\n",
    "print(\"Area=\", ls*ls, \"cm\")\n",
    "print(\"--------Area of\",shape2,\"--------\")\n",
    "print(\"Length= \",lr, \"cm\")\n",
    "print(\"Width= \",lw, \"cm\")\n",
    "print(\"Area= \",lw*lr, \"cm\")\n",
    "print(\"-----Circumference of\",shape3,\"-----\")\n",
    "print(\"Radius=\",cr ,\"cm\")\n",
    "print(\"Circumference=\", cr*2, \"cm\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "47b2ecdb",
   "metadata": {},
   "outputs": [],
   "source": [
    "a = \"i have a square with length of one side is 10 cm and a rectangle with length = 7.5 cm and width = 9 cm also calculate the area and circumference of a circle with radius of 2.5 cm\"\n",
    "shape1=a[9:15]\n",
    "shape2=a[55:64]\n",
    "shape3=a[150:156]\n",
    "b =a[42:45] #Square Extraction\n",
    "c =a[79:82] #Rectangle length Extraction\n",
    "d =a[98:99] #Rectangle Width Extraction\n",
    "e =a[172:175] #Circle Radius Extraction\n",
    "ls = int(b)\n",
    "lr = float(c)\n",
    "lw = int(d)\n",
    "cr = float(e)\n",
    "print(\"---------Area of\",shape1, \"---------\")\n",
    "print(\"Length= \",ls, \"cm\")\n",
    "print(\"Area=\", ls*ls, \"cm\")\n",
    "print(\"--------Area of\",shape2,\"--------\")\n",
    "print(\"Length= \",lr, \"cm\")\n",
    "print(\"Width= \",lw, \"cm\")\n",
    "print(\"Area= \",lw*lr, \"cm\")\n",
    "print(\"-----Circumference of\",shape3,\"-----\")\n",
    "print(\"Radius=\",cr ,\"cm\")\n",
    "print(\"Circumference=\", cr*2, \"cm\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d2c34777",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
