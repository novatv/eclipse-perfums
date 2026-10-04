# eclipseperfume.com → Railway

El dominio está en GoDaddy (registrado el 12-09-2025, DNS ns37/ns38.domaincontrol.com).
Railway ya tiene dados de alta `eclipseperfume.com` y `www.eclipseperfume.com` y espera estos registros.

## Registros a crear en GoDaddy (Mi dominio → DNS → Registros)

| Tipo | Nombre | Valor | TTL |
|---|---|---|---|
| CNAME | `www` | `qzccqcc8.up.railway.app` | 600 |
| TXT | `_railway-verify.www` | `railway-verify=2943f28f7f3bcd372b2a72b6a3e3ddb4183f9b58c8556e82174ef133abc26425` | 600 |
| TXT | `_railway-verify` | `railway-verify=c3655c881e79a3cda9d73f51bffb714292d2b242b97ee5888734c2cb9060ce43` | 600 |

Importante: ya existe un CNAME `www` que apunta a `eclipseperfume.com`. Hay que EDITARLO y poner `qzccqcc8.up.railway.app` (no crear uno nuevo).

## Raíz (eclipseperfume.com sin www)
GoDaddy no permite CNAME en la raíz. Opción recomendada: en GoDaddy → "Reenvío" (Forwarding) → reenviar `eclipseperfume.com` a `https://www.eclipseperfume.com` (301, permanente).
Si prefieres que la raíz también sirva directamente desde Railway, habría que mover el DNS a Cloudflare (gratis) y usar CNAME aplanado a `ridgzu1b.up.railway.app`.

## Comprobar
```bash
dig +short www.eclipseperfume.com CNAME
dig +short _railway-verify.www.eclipseperfume.com TXT
```
Railway activa el HTTPS solo, normalmente en menos de 30 minutos tras ver los registros.
