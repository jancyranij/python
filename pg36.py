x=input("Enter the value")
y=0
for i in range(len(x)):
    if ("," in x)or("." in x)or(";" in x)or(":" in x)or("<" in x)or(">" in x)or("/" in x)or("?" in x)or("'" in x)or("["in x)or("]"in x)or("{" in x)or("}" in x)or("~" in x)or("!" in x)or("@" in x)or("#" in x)or("$" in x)or("%"in x)or("^" in x)or("&" in x)or("*" in x)or("(" in x)or(")" in x)or("-" in x)or("+"in x)or("="in x):
            y=y+1
            print(y)
