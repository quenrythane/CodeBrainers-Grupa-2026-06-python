# 50 Przykładów Testów JavaScript w Postmanie dla Endpointu POST

Zbiór 50 profesjonalnych i praktycznych przykładów skryptów testowych w języku JavaScript przeznaczonych do użycia w narzędziu **Postman** (zakładka *Tests*) przy testowaniu endpointów typu **POST** (tworzenie/przetwarzanie zasobów).

---

## I. Kody Statusu (Status Codes)

### 1. Sprawdzenie statusu 201 Created (Standard dla POST)
```javascript
pm.test("Status code is 201 Created", function () {
    pm.response.to.have.status(201);
});
```

### 2. Sprawdzenie statusu 200 OK (Gdy POST zwraca 200 z obiektem)
```javascript
pm.test("Status code is 200 OK", function () {
    pm.response.to.have.status(200);
});
```

### 3. Weryfikacja nazwy statusu w odpowiedzi
```javascript
pm.test("Status text is Created", function () {
    pm.response.to.have.status("Created");
});
```

### 4. Sprawdzenie czy status mieści się w grupie sukcesu (2xx)
```javascript
pm.test("Status code is successful (2xx)", function () {
    pm.expect(pm.response.code).to.be.within(200, 299);
});
```

### 5. Sprawdzenie niepoprawnego żądania (400 Bad Request - scenariusz negatywny)
```javascript
pm.test("Status code is 400 Bad Request", function () {
    pm.response.to.have.status(400);
});
```

### 6. Sprawdzenie braku autoryzacji (401 / 403)
```javascript
pm.test("Status code is 401 Unauthorized", function () {
    pm.response.to.have.status(401);
});
```

---

## II. Nagłówki Odpowiedzi (Response Headers)

### 7. Weryfikacja nagłówka `Content-Type` (`application/json`)
```javascript
pm.test("Content-Type is application/json", function () {
    pm.response.to.have.header("Content-Type");
    pm.expect(pm.response.headers.get("Content-Type")).to.include("application/json");
});
```

### 8. Sprawdzenie obecności nagłówka `Location` (URL nowo utworzonego zasobu)
```javascript
pm.test("Response header includes Location", function () {
    pm.response.to.have.header("Location");
    pm.expect(pm.response.headers.get("Location")).to.match(/\/api\/v1\/users\/\d+/);
});
```

### 9. Sprawdzenie kodowania UTF-8 w nagłówku `Content-Type`
```javascript
pm.test("Content-Type charset is UTF-8", function () {
    pm.expect(pm.response.headers.get("Content-Type")).to.include("charset=utf-8");
});
```

### 10. Weryfikacja nagłówków bezpieczeństwa (`X-Content-Type-Options`)
```javascript
pm.test("Security header X-Content-Type-Options is nosniff", function () {
    pm.expect(pm.response.headers.get("X-Content-Type-Options")).to.eql("nosniff");
});
```

### 11. Sprawdzenie polityki pamięci podręcznej (`Cache-Control`)
```javascript
pm.test("Cache-Control header prevents caching", function () {
    pm.expect(pm.response.headers.get("Cache-Control")).to.include("no-store");
});
```

### 12. Brak wycieku informacji o serwerze (`X-Powered-By`)
```javascript
pm.test("X-Powered-By header is absent for security", function () {
    pm.response.to.not.have.header("X-Powered-By");
});
```

---

## III. Wydajność i Czas Odpowiedzi (Response Time SLA)

### 13. Czas odpowiedzi poniżej 500 ms
```javascript
pm.test("Response time is less than 500ms", function () {
    pm.expect(pm.response.responseTime).to.be.below(500);
});
```

### 14. Rygorystyczny SLA: Czas odpowiedzi poniżej 200 ms
```javascript
pm.test("Response time meets strict SLA (<200ms)", function () {
    pm.expect(pm.response.responseTime).to.be.below(200);
});
```

### 15. Sprawdzenie metryk wydajnościowych w `Server-Timing`
```javascript
pm.test("Server-Timing header is present", function () {
    pm.response.to.have.header("Server-Timing");
});
```

---

## IV. Struktura i Typy Danych JSON (Body & Data Types)

### 16. Weryfikacja, czy odpowiedź jest poprawnym obiektem JSON
```javascript
pm.test("Response body is a valid JSON object", function () {
    pm.response.to.be.json;
    const responseJson = pm.response.json();
    pm.expect(responseJson).to.be.an("object");
});
```

### 17. Obecność identyfikatora `id` w odpowiedzi
```javascript
pm.test("Response includes newly generated id", function () {
    const jsonData = pm.response.json();
    pm.expect(jsonData).to.have.property("id");
});
```

### 18. Typ danych: `id` jest liczbą dodatnią
```javascript
pm.test("Generated id is a positive integer", function () {
    const jsonData = pm.response.json();
    pm.expect(jsonData.id).to.be.a("number");
    pm.expect(jsonData.id).to.be.above(0);
});
```

### 19. Format UUID v4 dla pola `id`
```javascript
pm.test("Generated id is a valid UUID v4", function () {
    const jsonData = pm.response.json();
    const uuidRegex = /^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/i;
    pm.expect(jsonData.id).to.match(uuidRegex);
});
```

### 20. Sprawdzenie typu danych dla pola tekstowego (`name`)
```javascript
pm.test("Field 'name' is a non-empty string", function () {
    const jsonData = pm.response.json();
    pm.expect(jsonData.name).to.be.a("string").that.is.not.empty;
});
```

### 21. Sprawdzenie wartości typu boolean (`isActive`)
```javascript
pm.test("Field 'isActive' is boolean and true", function () {
    const jsonData = pm.response.json();
    pm.expect(jsonData.isActive).to.be.a("boolean").and.to.be.true;
});
```

### 22. Sprawdzenie tablicy i jej długości (`tags`)
```javascript
pm.test("Field 'tags' is an array with items", function () {
    const jsonData = pm.response.json();
    pm.expect(jsonData.tags).to.be.an("array").that.is.not.empty;
});
```

### 23. Brak wartości `null` w kluczowych polach
```javascript
pm.test("Mandatory fields are not null", function () {
    const jsonData = pm.response.json();
    pm.expect(jsonData.email).to.not.be.null;
    pm.expect(jsonData.role).to.not.be.null;
});
```

### 24. Datastamp: Sprawdzenie formatu ISO 8601 (`createdAt`)
```javascript
pm.test("Field 'createdAt' is a valid ISO 8601 date string", function () {
    const jsonData = pm.response.json();
    const isoDateRegex = /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d+)?(Z|[+-]\d{2}:\d{2})$/;
    pm.expect(jsonData.createdAt).to.match(isoDateRegex);
});
```

### 25. Data utworzenia wpisu nie pochodzi z przyszłości
```javascript
pm.test("'createdAt' timestamp is not in the future", function () {
    const jsonData = pm.response.json();
    const createdDate = new Date(jsonData.createdAt).getTime();
    const now = new Date().getTime();
    pm.expect(createdDate).to.be.at.most(now + 1000); // 1s zapasu na różnice zegarów
});
```

---

## V. Logika Biznesowa i Zgodność Payloadu (Payload Matching)

### 26. Dane w odpowiedzi zgadzają się z danymi wysłanymi w Request Body
```javascript
pm.test("Response body matches request payload", function () {
    const reqData = JSON.parse(pm.request.body.raw);
    const resData = pm.response.json();
    
    pm.expect(resData.name).to.eql(reqData.name);
    pm.expect(resData.email).to.eql(reqData.email);
});
```

### 27. Walidacja pól kalkulowanych (np. `totalPrice = price * quantity`)
```javascript
pm.test("Calculated total price matches price * quantity", function () {
    const jsonData = pm.response.json();
    const expectedTotal = jsonData.price * jsonData.quantity;
    pm.expect(jsonData.totalPrice).to.eql(expectedTotal);
});
```

### 28. Ustawienie wartości domyślnej dla pominiętego pola opcjonalnego
```javascript
pm.test("Default role is assigned when omitted in request", function () {
    const jsonData = pm.response.json();
    pm.expect(jsonData.role).to.eql("USER");
});
```

### 29. Czyszczenie białych znaków na brzegach tekstów (Trim check)
```javascript
pm.test("String fields are automatically trimmed", function () {
    const jsonData = pm.response.json();
    pm.expect(jsonData.username).to.eql(jsonData.username.trim());
});
```

### 30. Domyślny status nowo utworzonego obiektu
```javascript
pm.test("New resource has default status PENDING", function () {
    const jsonData = pm.response.json();
    pm.expect(jsonData.status).to.eql("PENDING");
});
```

### 31. Poprawna obsługa znaków specjalnych i Unicode (UTF-8)
```javascript
pm.test("Unicode characters are correctly stored and returned", function () {
    const reqData = JSON.parse(pm.request.body.raw);
    const jsonData = pm.response.json();
    pm.expect(jsonData.description).to.eql(reqData.description);
});
```

### 32. Sprawdzenie struktury osadzonego obiektu (Nested Object)
```javascript
pm.test("Nested object 'address' contains correct structure", function () {
    const jsonData = pm.response.json();
    pm.expect(jsonData).to.have.property("address");
    pm.expect(jsonData.address).to.have.all.keys("street", "city", "zipCode");
});
```

### 33. Sprawdzenie unikalności elementów w zwróconej tablicy
```javascript
pm.test("Returned list of permissions has unique items", function () {
    const jsonData = pm.response.json();
    const uniquePermissions = new Set(jsonData.permissions);
    pm.expect(uniquePermissions.size).to.eql(jsonData.permissions.length);
});
```

---

## VI. Zmienne Postmana i Chaining (Workflow)

### 34. Zapisanie utworzonego `id` do zmiennej środowiskowej
```javascript
pm.test("Save created ID to environment variable", function () {
    const jsonData = pm.response.json();
    pm.expect(jsonData.id).to.exist;
    pm.environment.set("created_user_id", jsonData.id);
});
```

### 35. Zapisanie tokenu wygenerowanego po POST (np. /login /register)
```javascript
pm.test("Save bearer token to collection variable", function () {
    const jsonData = pm.response.json();
    pm.expect(jsonData.accessToken).to.be.a("string");
    pm.collectionVariables.set("auth_token", jsonData.accessToken);
});
```

### 36. Porównanie odpowiedzi ze zmienną ze środowiska
```javascript
pm.test("Created user belongs to expected tenantId", function () {
    const jsonData = pm.response.json();
    const expectedTenant = pm.environment.get("tenant_id");
    pm.expect(jsonData.tenantId).to.eql(expectedTenant);
});
```

### 37. Zapisanie pełnego payloadu odpowiedzi jako JSON w zmiennej
```javascript
pm.test("Cache response body into environment", function () {
    pm.environment.set("last_created_resource", JSON.stringify(pm.response.json()));
});
```

### 38. Usunięcie zmiennej tymczasowej po udanym requeście
```javascript
pm.test("Clean up temporary request variables", function () {
    pm.environment.unset("temp_request_payload");
});
```

### 39. Upewnienie się, że nowe ID różni się od starego zapisanego w środowisku
```javascript
pm.test("New ID is different from previous run ID", function () {
    const jsonData = pm.response.json();
    const oldId = pm.environment.get("created_user_id");
    pm.expect(jsonData.id).to.not.eql(oldId);
});
```

### 40. Zmiana przepływu Runnera (Dynamic Chaining - `setNextRequest`)
```javascript
pm.test("Set next request to Fetch User Details", function () {
    if (pm.response.code === 201) {
        pm.execution.setNextRequest("Get User Details");
    } else {
        pm.execution.setNextRequest(null); // Zakończ runnera przy błędzie
    }
});
```

---

## VII. Scenariusze Negatywne i Edge Cases

### 41. Weryfikacja komunikatu błędu dla braku wymaganego pola (400)
```javascript
pm.test("Error response contains missing field validation message", function () {
    pm.response.to.have.status(400);
    const jsonData = pm.response.json();
    pm.expect(jsonData.message).to.include("Field 'email' is required");
});
```

### 42. Walidacja formatu e-mail (422 Unprocessable Entity)
```javascript
pm.test("Returns 422 for invalid email format", function () {
    pm.response.to.have.status(422);
    const jsonData = pm.response.json();
    pm.expect(jsonData.errors).to.be.an("array");
    pm.expect(jsonData.errors[0].field).to.eql("email");
});
```

### 43. Sprawdzenie ustandaryzowanej struktury błędu (Problem Details / RFC 7807)
```javascript
pm.test("Error response follows RFC 7807 problem details structure", function () {
    const jsonData = pm.response.json();
    pm.expect(jsonData).to.have.all.keys("type", "title", "status", "detail", "instance");
});
```

### 44. Sprawdzenie błędu duplikacji zasobu (409 Conflict)
```javascript
pm.test("Status code is 409 Conflict on duplicate creation", function () {
    pm.response.to.have.status(409);
    const jsonData = pm.response.json();
    pm.expect(jsonData.code).to.eql("RESOURCE_ALREADY_EXISTS");
});
```

### 45. Odrzucenie zbyt dużego payloadu (413 Payload Too Large)
```javascript
pm.test("Returns 413 when payload exceeds limit", function () {
    pm.response.to.have.status(413);
});
```

### 46. Nieobsługiwany typ mediów (415 Unsupported Media Type)
```javascript
pm.test("Returns 415 when Content-Type is text/plain", function () {
    pm.response.to.have.status(415);
});
```

### 47. Bezpieczeństwo XSS: Kod HTML w tekście zostaje escaped/sanitowany
```javascript
pm.test("Response sanitizes dangerous HTML tags", function () {
    const jsonData = pm.response.json();
    pm.expect(jsonData.bio).to.not.include("<script>");
});
```

---

## VIII. Zaawansowane Schematy JSON i Narzędzia JS

### 48. Walidacja pełnego schematu JSON (JSON Schema Draft-07)
```javascript
pm.test("Response matches strict JSON Schema", function () {
    const schema = {
        "type": "object",
        "required": ["id", "username", "email", "createdAt"],
        "properties": {
            "id": { "type": "integer", "minimum": 1 },
            "username": { "type": "string", "minLength": 3 },
            "email": { "type": "string", "format": "email" },
            "createdAt": { "type": "string" }
        }
    };
    pm.response.to.have.jsonSchema(schema);
});
```

### 49. Iteracja po tablicy w odpowiedzi i walidacja każdego obiektu
```javascript
pm.test("Every item in created batch has valid status and id", function () {
    const jsonData = pm.response.json();
    pm.expect(jsonData.items).to.be.an("array");
    
    jsonData.items.forEach((item, index) => {
        pm.expect(item.id, `Item at index ${index} missing id`).to.be.above(0);
        pm.expect(item.status, `Item at index ${index} invalid status`).to.eql("CREATED");
    });
});
```

### 50. Zaawansowane logowanie diagnostyczne do konsoli Postmana
```javascript
pm.test("Diagnostic logging on test failure", function () {
    const responseCode = pm.response.code;
    const responseTime = pm.response.responseTime;
    
    if (responseCode !== 201) {
        console.error(`[FAIL] Expected 201 Created but got ${responseCode}`);
        console.log("Response Body:", pm.response.text());
    } else {
        console.info(`[PASS] Resource created in ${responseTime}ms`);
    }
    
    pm.response.to.have.status(201);
});
```
