# Variables in PowerShell

Variables in [[PowerShell]] are specified by putting a dollar sign (`$`) in front of their name such as `$apples, $oranges`, etc. 

>[!TIP]+ How-To: Create a Variable
>
>```powershell
>$var = val
>```
>
>![[res/Create Variable.png]]
>

It is important to note that all PowerShell variables are .NET objects and we can call methods on them via the `$var.method()` syntax.

## Type Casting

Variables (and literal values, too) can be converted between different types in PowerShell by prepending them with the cast operator `[<type>]`- for example, `[IPAddress]"10.10.11.29"`, `[float]$apples`.

![[res/Cast Variable.png]]

If the value does not represent a valid object of the type `<type>`, then PowerShell will return an error.

![[res/Cast Error.png]]