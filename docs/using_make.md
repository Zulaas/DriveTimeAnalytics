#Linux

#Windows

make is a GNU command so the only way you can get it on Windows is installing a Windows version like the one provided
 by GNUWin32. Anyway, there are several options for getting that:

Using MinGW, be sure you have C:\MinGW\bin\mingw32-make.exe. Otherwise you're missing the mingw32-make additional
 utilities. Look for the link at MinGW's HowTo page to get it installed. Once you've got it, you have two choices:
1.1 Copy the MinGW make executable to make.exe:

copy c:\MinGW\bin\mingw32-make.exe c:\MinGW\bin\make.exe
1.2 Create a link to the actual executable, in your PATH. In this case, if you update MinGW, the link is not deleted:

mklink c:\bin\make.exe C:\MinGW\bin\mingw32-make.exe
Other option is using Chocolatey. First you need to install this package manager. Once installed you simlpy need to 
install make:

choco install make
Last option is installing a Windows Subsystem for Linux (WSL), so you'll have a Linux distribution of your choice 
embedded in Windows 10 where you'll be able to install make, gccand all the tools you need to build C programs.