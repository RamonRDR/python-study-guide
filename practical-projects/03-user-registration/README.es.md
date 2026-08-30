<div align="center">

# Proyecto 03 · Registro de Usuarios

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Volver a Proyectos Prácticos](../README.es.md)

Este es el tercer proyecto de la **Fase 10: Proyectos Prácticos**. Se centra en validación de datos similares a identidad, valores canónicos, prevención de duplicados, búsquedas indexadas, actualizaciones seguras, estados explícitos de cuenta y límites claros de servicio, sin introducir autenticación real ni datos personales.

**Tiempo estimado de estudio e implementación:** 180–240 minutos.

## Objetivos de aprendizaje

Al terminar este proyecto, deberías poder:

- convertir reglas de entrada en funciones explícitas de validación;
- distinguir datos de presentación de identificadores canónicos;
- normalizar Unicode y espacios de forma intencional;
- impedir duplicados después de la normalización;
- mantener varios índices de búsqueda sin exponer diccionarios internos;
- actualizar campos indexados sin dejar claves antiguas;
- modelar el ciclo de vida de una cuenta con enum y transiciones explícitas;
- separar snapshots inmutables de usuario de un servicio de registro mutable;
- probar seguridad de mutación, búsquedas, límites y transiciones inválidas.

## 1. Desafío del proyecto

Construye un registro en memoria capaz de:

1. registrar usuarios ficticios;
2. asignar IDs positivos secuenciales;
3. normalizar nombre, username e identificador de correo;
4. impedir usernames y correos duplicados después de la canonicalización;
5. localizar usuarios por ID, username o correo;
6. buscar dentro de los campos de identidad;
7. actualizar nombre, username y correo de forma segura;
8. mantener sincronizados los índices de username y correo después de cambios;
9. suspender, reactivar o desactivar usuarios siguiendo reglas explícitas;
10. demostrar comportamientos correctos e incorrectos con pruebas automatizadas.

## 2. Contrato de datos

Cada usuario contiene:

```text
user_id   -> entero positivo generado por el registro
full_name -> texto normalizado y no vacío, con un máximo de 80 caracteres
username  -> identificador canónico de 3 a 30 caracteres
email     -> identificador canónico de correo según las reglas del proyecto
status    -> active, suspended o deactivated
```

El proyecto usa únicamente datos ficticios de demostración.

## 3. Por qué importan los valores canónicos

Estas entradas deben representar el mismo username:

```text
Maya.Chen
maya.chen
  MAYA.CHEN  
```

Si la unicidad se verifica antes de normalizar, valores equivalentes pueden entrar como cuentas separadas.

`normalize_username(...)` convierte la entrada en una representación canónica antes de búsquedas o verificaciones de duplicados.

## 4. Normalización Unicode

El proyecto usa normalización Unicode **NFKC** antes de validar texto similar a identidad.

Por ejemplo:

```text
ＡＢＣ
```

se normaliza a:

```text
ABC
```

NFKC es una decisión de aplicación en este proyecto. Los sistemas reales deben elegir su política de normalización según sus propios requisitos de identidad.

## 5. Normalización del nombre

El nombre conserva una capitalización legible, pero normaliza los espacios:

```python
normalize_full_name("  Maya   Chen  ")
# "Maya Chen"
```

Se rechazan valores vacíos y nombres por encima del límite del proyecto.

El nombre es un dato de presentación y no se usa como clave única.

## 6. Contrato de username

Los usernames:

- se normalizan con NFKC;
- eliminan espacios externos;
- se convierten con `casefold()`;
- se limitan a 3–30 caracteres ASCII;
- deben comenzar con una letra o un dígito;
- solo pueden contener letras, dígitos, `.`, `_` y `-`.

Ejemplos:

```text
Maya.Chen -> maya.chen
NOAH-R    -> noah-r
```

Estas son reglas del proyecto, no reglas universales de username.

## 7. Contrato de correo electrónico

Este proyecto implementa intencionalmente una **política restringida de identificador de correo a nivel de aplicación**, no un parser completo de todos los estándares RFC de correo.

El registro:

- elimina espacios en los extremos;
- aplica NFKC y `casefold()`;
- exige exactamente un `@`;
- rechaza espacios dentro de la dirección;
- valida un conjunto restringido de caracteres ASCII en la parte local;
- rechaza puntos iniciales, finales o repetidos en la parte local;
- convierte dominios Unicode con el codec IDNA de Python;
- exige un dominio separado por puntos con etiquetas válidas;
- aplica límites de longitud definidos por el proyecto.

Ejemplo:

```python
normalize_email("MAYA@Example.COM")
# "maya@example.com"
```

Un dominio Unicode puede convertirse a forma ASCII IDNA:

```python
normalize_email("user@bücher.example")
# "user@xn--bcher-kva.example"
```

El proyecto trata el correo canónico completo como case-insensitive para unicidad. Los sistemas reales pueden necesitar otros requisitos.

## 8. Modelo inmutable `User`

`User` es una dataclass congelada:

```python
@dataclass(frozen=True, slots=True)
class User:
    user_id: int
    full_name: str
    username: str
    email: str
    status: UserStatus = UserStatus.ACTIVE
```

La validación también se ejecuta cuando se usa directamente el constructor de la dataclass.

El registro no modifica un objeto `User` existente. Los cambios crean un nuevo snapshot.

## 9. Límites del servicio de registro

`UserRegistry` concentra el comportamiento mutable de la colección:

```text
registro
lookup
búsqueda
cambio de campos indexados
cambio de nombre visible
transiciones de estado
```

`User` describe un snapshot válido. El registro coordina relaciones entre varios usuarios.

Esto evita esconder reglas globales de unicidad dentro de un único registro que no conoce toda la colección.

## 10. IDs secuenciales sin huecos por registros rechazados

`register(...)` crea y valida un candidato antes de alterar el estado del registro.

Si el username o correo ya está ocupado, el registro falla y el siguiente ID **no** se consume.

```text
usuario válido -> ID 1
duplicado rechazado -> no consume ID
siguiente usuario válido -> ID 2
```

Este comportamiento es una convención del proyecto para hacer visible y comprobable el orden de mutación.

## 11. Prevención de duplicados

El registro mantiene índices canónicos:

```text
username -> user_id
email    -> user_id
```

Por eso estos usernames colisionan:

```text
maya.chen
MAYA.CHEN
```

Y estos correos también colisionan según la política del proyecto:

```text
maya@example.com
MAYA@EXAMPLE.COM
```

Un duplicado genera `DuplicateUserError` antes de alterar el estado.

## 12. Búsqueda indexada

El registro ofrece:

```python
registry.get_by_id(1)
registry.get_by_username("MAYA.CHEN")
registry.get_by_email("maya@EXAMPLE.COM")
```

Las entradas de lookup pasan por las mismas funciones de canonicalización utilizadas en el registro.

Los valores ausentes generan `UserNotFoundError` en vez de exponer un `KeyError` crudo de diccionario.

## 13. Búsqueda

`search(...)` realiza una búsqueda case-insensitive por substring sobre:

- nombre completo;
- username canónico;
- correo canónico.

Los resultados conservan el orden de registro.

Un filtro opcional de `UserStatus` puede reducir el conjunto:

```python
registry.search("example", status=UserStatus.ACTIVE)
```

Es una implementación simple en memoria para aprendizaje, no un motor de búsqueda completo.

## 14. Actualización segura de campos indexados

Cambiar username o correo implica dos responsabilidades:

1. validar y comprobar que el nuevo valor está disponible;
2. sustituir la clave antigua del índice por la nueva.

El proyecto valida primero y solo después modifica los índices.

Una actualización rechazada por duplicado mantiene funcionando la clave anterior.

## 15. Ciclo de vida de la cuenta

Estados soportados:

```text
active
suspended
deactivated
```

Transiciones permitidas:

```text
active    -> suspended
suspended -> active
active    -> deactivated
suspended -> deactivated
```

`deactivated` es terminal en esta versión.

Las transiciones inválidas generan `InvalidUserTransitionError`.

## 16. Por qué usar enum

`UserStatus` es un enum, no texto arbitrario.

Eso impide estados como:

```text
"actve"
"paused-ish"
"disabled maybe"
```

de entrar silenciosamente en el modelo.

Los enums son útiles cuando un campo tiene un conjunto pequeño y explícito de valores válidos.

## 17. Estructura del proyecto

```text
03-user-registration/
├── README.md
├── README.pt-BR.md
├── README.es.md
├── user_registration.py
├── demo.py
└── tests/
    ├── conftest.py
    └── test_user_registration.py
```

## 18. Ejecutar la demo determinista

Desde la raíz del repositorio:

```bash
python practical-projects/03-user-registration/demo.py
```

Salida esperada:

```text
users: 3
active: 2
suspended: 1
lookup: maya.chen
search-example: 3
```

## 19. Ejecutar las pruebas

```bash
python -m pytest -q practical-projects/03-user-registration/tests
```

La suite inicial contiene **46 escenarios pytest** que cubren normalización, reglas restringidas de correo, duplicados, IDs generados, registros inicializados, lookup, búsqueda, actualizaciones seguras, snapshots inmutables y transiciones del ciclo de vida.

## 20. Caminos de error para inspeccionar manualmente

Prueba:

```python
registry.register("Maya Chen", "ab", "maya@example.com")
registry.register("Maya Chen", "maya", "not-an-email")
registry.register("Other User", "MAYA", "other@example.com")
registry.get_by_id(999)
registry.reactivate(1)
```

Lee las excepciones y revisa el estado del registro después de cada operación rechazada.

## 21. Nota de diseño: validación y unicidad son problemas diferentes

Un username puede ser sintácticamente válido y aun así no estar disponible porque otro usuario ya posee el mismo valor canónico.

Validación responde:

> ¿Este valor tiene una estructura aceptable?

Unicidad responde:

> ¿Este valor aceptable está disponible en esta colección?

Separar esas preguntas hace el código más claro y comprobable.

## 22. Nota de diseño: los índices son estado derivado

Los diccionarios de username y correo son índices secundarios derivados de los valores canónicos de `User`.

Cuando un campo indexado cambia, el mapa principal de usuarios y el índice correspondiente deben seguir siendo consistentes.

Este es un pequeño ejemplo de invariante: distintas partes del estado deben concordar en todo momento.

## 23. Nota de diseño: validar antes de mutar

El registro y las actualizaciones de identidad siguen la misma secuencia:

```text
normalizar -> validar -> comprobar conflictos -> crear reemplazo -> mutar
```

Este orden reduce errores de actualización parcial.

## 24. Lo que el proyecto no incluye

Esta versión no incluye:

- contraseñas;
- hashing de contraseñas;
- sesiones de login;
- autenticación;
- autorización o roles;
- datos personales reales;
- envío de correo o enlaces de verificación;
- persistencia o base de datos;
- proveedores externos de identidad;
- API web;
- GUI.

Estos temas introducen otras preocupaciones de seguridad e infraestructura. El proyecto permanece enfocado en reglas de dominio en memoria.

## 25. Nota de seguridad

Un sistema real de registro no debe guardar contraseñas en texto plano y requeriría mucho más trabajo de seguridad que este registro educativo.

No trates este proyecto como una implementación de autenticación lista para producción.

## 26. Desafío de extensión: eventos de auditoría

Registra eventos ficticios como:

```text
user_registered
username_changed
user_suspended
user_reactivated
user_deactivated
```

Mantén el registro de eventos separado del snapshot principal de usuario.

## 27. Desafío de extensión: política configurable de username

Extrae las reglas de username a un objeto de política configurable con:

- rango de longitud;
- separadores permitidos;
- permiso o no de dígito como primer carácter.

Mantén la lógica de unicidad independiente de la política de sintaxis.

## 28. Desafío de extensión: adaptador de persistencia

Agrega una interfaz de repositorio y un adaptador JSON o SQLite sin mover las reglas de validación a la capa de persistencia.

El registro en memoria debe seguir siendo comprobable sin I/O.

## 29. Discusión de portafolio

Al presentar este proyecto, explica las decisiones de ingeniería y no solo “registra usuarios”:

- identificadores canónicos antes de comprobar unicidad;
- política explícita y restringida de correo;
- normalización Unicode e IDNA;
- snapshots inmutables;
- responsabilidades separadas entre modelo y servicio;
- índices secundarios para lookup;
- actualización atómica de campos indexados;
- máquina de estados explícita;
- excepciones de dominio;
- pruebas centradas en mutación.

## 30. Checklist de revisión

Antes de considerar terminada tu implementación, comprueba:

- ¿Usernames equivalentes pueden evitar duplicados cambiando mayúsculas o espacios?
- ¿Lookup y duplicidad de correo usan el mismo contrato de canonicalización?
- ¿Un registro rechazado conserva la secuencia de IDs?
- ¿Los cambios de username y correo eliminan índices antiguos?
- ¿Una actualización rechazada conserva el índice válido anterior?
- ¿Los estados se limitan a valores explícitos del enum?
- ¿Las transiciones inválidas son rechazadas?
- ¿Los diccionarios internos permanecen ocultos?
- ¿Las contraseñas y los datos personales reales están intencionalmente ausentes?
- ¿Las pruebas demuestran caminos correctos y de error?

## 31. Próximo proyecto

El Proyecto 03 añade identidad canónica, prevención de duplicados, índices secundarios, actualizaciones seguras y transiciones de ciclo de vida a la progresión de la Fase 10.

El siguiente proyecto planificado es **CSV Analyzer**, que cambiará el foco hacia entrada tabular, expectativas de esquema, validación por fila, agregaciones, datos malformados y análisis determinista.
