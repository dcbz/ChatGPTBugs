#
#@author dcbz
#@category 
#@keybinding
#@menupath
#@toolbar

from ghidra.app.decompiler.flatapi import FlatDecompilerAPI
from ghidra.program.flatapi import FlatProgramAPI
#from chatgpt import Conversation
import json
import httplib

CHATGPTSRVPORT = 4321

fpapi = FlatProgramAPI(getState().getCurrentProgram())
fdapi = FlatDecompilerAPI(fpapi)

func = currentProgram.getFunctionManager().getFunctionContaining(currentAddress);
print("[+] Decompiling {}".format(func.name))

src = fdapi.decompile(func)

print("[+] Contacting ChatGPT to find all the bugs!")

msg = "Find all the bugs in ```" + src + "```"
hdr = {"content-type": "application/json"}
#conn = httplib.HTTPConnection("http://localhost:%u" % CHATGPTSRVPORT)
conn = httplib.HTTPConnection("127.0.0.1:4321")
conn.request('POST', '/chat', json.dumps(msg), hdr)
response = conn.getresponse()
data = response.read() 
print(data)