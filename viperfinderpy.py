import requests
# subdomain finder
# made by Renua
def subfind(domain_name, subdomains_name):
  for subdomain in subdomains_name:
    url = "https://{}.{}".format(subdomain, domain_name)
    try:
      requests.get(url)
    except:
      requests.ConnectionError
      print(f'[+] {url}')

      pass
print(""" ---_ ......._-_--.
      (|\ /      / /| \  \
      /  /     .'  -=-'   `.
     /  /    .'             )
   _/  /   .'        _.)   /
  / o   o        _.-' /  .'
  \          _.-'    / .'*|
   \______.-'//    .'.' \*|
    \|  \ | //   .'.' _ |*|
     `   \|//  .'.'_ _ _|*|
      .  .// .'.' | _ _ \*|
      \`-|\_/ /    \ _ _ \*\
       `/'\__/      \ _ _ \*\
      /^|            \ _ _ \*
     '  `             \ _ _ \  
                       \_""")
dom = input("-------Enter a valid domain---------\n")
filename = input("---Enter a file name---\n")
with open('subdomains_n.txt', 'r') as text:
  name = text.read()
  sub = name.splitlines()
  f = open(filename, "a")
  f.write(subfind(dom, sub))
  f.close()
