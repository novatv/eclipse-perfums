# eclipseperfume.es → Railway

Registros DNS que hay que crear en el registrador del dominio (Porkbun, GoDaddy, Namecheap…).
Railway ya tiene los dos nombres dados de alta y espera a verlos en DNS para emitir el certificado HTTPS.

| Tipo | Nombre (host) | Valor |
|---|---|---|
| CNAME (o ALIAS/ANAME en la raíz) | `@` (eclipseperfume.es) | `0idrsghi.up.railway.app` |
| TXT | `_railway-verify` | `railway-verify=02333393e74b729982ec5eb45d4f81083aaf4f7bce26de2abaf5365acb971516` |
| CNAME | `www` | `cee5dtoh.up.railway.app` |
| TXT | `_railway-verify.www` | `railway-verify=23824d52370b4ea1fb7b97f23e76bb3641d8796276ae7e82b4641ca159b0b162` |

Notas
- La raíz (`@`) no admite CNAME en todos los registradores. Porkbun y Cloudflare sí (ALIAS / CNAME flattening). Si el tuyo no, usa solo `www` y pide una redirección de `eclipseperfume.es` a `www.eclipseperfume.es` en el registrador.
- Tras guardar los registros, Railway verifica en 5-30 minutos y activa HTTPS solo.
- Comprobar: `dig +short eclipseperfume.es CNAME` y `dig +short www.eclipseperfume.es CNAME`.
