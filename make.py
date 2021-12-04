
#
#	https://spdx.org/licenses/MIT.html
#	https://opensource.org/licenses/MIT
#
#	Full name: MIT License
#	Short identifier: MIT
#
#	Copyright (c) 2021 - 2022 Lyan.
#
#	Permission is hereby granted, free of charge, to any person obtaining a copy
#	of this software and associated documentation files (the "Software"), to deal
#	in the Software without restriction, including without limitation the rights
#	to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#	copies of the Software, and to permit persons to whom the Software is
#	furnished to do so, subject to the following conditions:
#	The above copyright notice and this permission notice shall be included in all
#	copies or substantial portions of the Software.
#	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#	IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#	FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#	AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#	LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#	OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#	SOFTWARE.
#

from datetime import datetime
from datetime import date
import subprocess

old_contents = []
minor_build = 0

# Path to folder with your server files, e.g: E:/samp-server.
path = ""

build = open(f'{path}/gamemodes/src/build/version.inc', 'r')
count = 0;

for line in build:
    old_contents.append(line.strip())

build.close()

for word in old_contents[3].split():
   if word.isdigit():
      minor_build = int(word)

today = date.today()
now = datetime.now()

major_build = today.strftime("%Y")
df = today.strftime("%d.%m.%Y")
hf = now.strftime("%H:%M")
minor_build += 1

info = [
    f"#define BUILD_DATE     \"{df}\"\n",
    f"#define BUILD_TIME     \"{hf}\"\n",
    f"#define BUILD_MAJOR    {major_build}\n",
    f"#define BUILD_MINOR    {minor_build}\n",
    "#define AUTHOR         \"Lyan\"\n"
]

build = open(f'{path}/gamemodes/src/build/version.inc', 'w')
build.writelines(info)
build.close()

subprocess.run(f"{path}/build/pawncc.exe {path}\gamemodes\main.pwn -Dgamemodes -;+ -(+ -d3 -Z+")
