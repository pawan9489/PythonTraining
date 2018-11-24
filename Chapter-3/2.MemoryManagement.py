# Literals - 

x = 10

y = x

print("x = {0} -> {1}\ny = {2} -> {3}".format(x, id(x), y, id(y)))

x = x + 1
print()
print("x = {0} -> {1}\ny = {2} -> {3}".format(x, id(x), y, id(y)))

z = 10
print()
print(
    "x = {0} -> {1}\ny = {2} -> {3}\nz = {4} -> {5}".format(
        x, id(x), y, id(y), z, id(z)
    )
)

print()
a = [1, 2, 3, 4, 5]
b = 1
print(id(b))
print(id(a[0]))

"""
CPP - https://www.onlinegdb.com/online_c++_compiler

int main()
{
    string x = "apple";
    string y = x;
    
    cout << "x = " << x << " - " << &x << endl;
    cout << "y = " << y << " - " << &y << endl;
    
    x = x + " Banana";
    cout << endl;
    cout << "x = " << x << " - " << &x << endl;
    cout << "y = " << y << " - " << &y << endl;
    
    string z = "apple Banana";
    cout << endl;
    cout << "x = " << x << " - " << &x << endl;
    cout << "y = " << y << " - " << &y << endl;
    cout << "z = " << z << " - " << &z << endl;
    return 0;
}

Output:
x = apple - 0x7ffe313456f0                     
y = apple - 0x7ffe31345700       

x = apple Banana - 0x7ffe313456f0                                           
y = apple - 0x7ffe31345700       

x = apple Banana - 0x7ffe313456f0
y = apple - 0x7ffe31345700                                                  
z = apple Banana - 0x7ffe31345720

"""

"""
C# 

static void Main(string[] args)
{
    string x = "apple";
    string y = x;
    Console.WriteLine(string.Format("x = {0} - {1}\ny = {2} - {3}\n", x, x.GetHashCode(), y, y.GetHashCode()));
    
    x = x + " Banana";
    Console.WriteLine(string.Format("x = {0} - {1}\ny = {2} - {3}\n", x, x.GetHashCode(), y, y.GetHashCode()));

    string z = "apple Banana";
    Console.WriteLine(string.Format("x = {0} - {1}\ny = {2} - {3}\nz = {4} - {5}\n", 
        x, x.GetHashCode(), y, y.GetHashCode(), z, z.GetHashCode()));

    List<string> str = new List<string>() { "a", "b", "c" };
    string a = "a";
    Console.WriteLine(string.Format("a = {0} - {1}\nstr[0] = {2} - {3}",
        a, a.GetHashCode(), str[0], str[0].GetHashCode()));

    Console.ReadLine();
}

Output:

x = apple - 1657858284
y = apple - 1657858284

x = apple Banana - 24126307
y = apple - 1657858284

x = apple Banana - 24126307
y = apple - 1657858284
z = apple Banana - 24126307

a = a - -842352705
str[0] = a - -842352705
"""

