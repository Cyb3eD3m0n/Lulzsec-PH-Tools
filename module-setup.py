import os, sys, time

print '''
{G}    .;'                      `;,    {G}[+]{N} Laughing At Your Security Since 2011
{G}  .;'  ,;'               `;,  `;,    {Y}_          _      ____        _       _ _{G}
{G} .;'  ,;'  ,;'   {Y}_{G}   `;,  `;,  `;,  {Y}| |   _   _| |____/ ___| _ __ | | ___ (_) |_{G}
{G} ::   ::   :    {Y}(_){G}    :   ::   ::  {Y}| |  | | | | |_  /\___ \| '_ \| |/ _ \| | __|{G}
{G} ':.  ':.  ':.  {Y}/_\{G}  ,;'  ,:'  ,:'  {Y}| |__| |_| | |/ /  ___) | |_) | | (_) | | |_{G}
{G}  ':.  ':.     {Y}/___\{G}     ,:'  ,:'   {Y}|_____\__,_|_/___||____/| .__/|_|\___/|_|\__|{G}
{G}    ':.       {Y}/_____\{G}        ,:'                            {Y}|_|
             {Y}/       \{N}

{G}[+]{Y} LulzSploit Setup For Termux{N}
{G}[+]{Y} LulzSploit v.3.5{N}


'''.format(Y = Y, G = G, N = N)
print "=" * 47
print ("\n\033[1;32m[+] \033[0mmodule-setup.py is running...\n")
os.system("unzip tools.zip")
print "=" * 47
os.system("pip2 install -r lulz-requirements.txt")
os.system("chmod +x lulzsploit.py")
print "=" * 47
print ("\n\033[1;32m[+] \033[0mmodule-setup.py is done!\n")
sys.exit()