#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
from webapp2_extras import jinja2

class MainHandler(webapp2.RequestHandler):
    def post(self):
        CIF = self.request.get("edCIF")
        nombre = self.request.get("edNombre")
        direccion = self.request.get("edDireccion")
        poblacion = self.request.get("edPoblacion")
        provincia = self.request.get("edProvincia")
        codPostal = self.request.get("edCodPostal")
        pais = self.request.get("edPais")
        contacto = self.request.get("edContacto")
        telefono = self.request.get("edTelefono")
        CIFCliente = self.request.get("edCIF1")
        nombreCliente = self.request.get("edNombre1")
        direccionCliente = self.request.get("edDireccion1")
        poblacionCliente = self.request.get("edPoblacion1")
        provinciaCliente = self.request.get("edProvincia1")
        codPostalCliente = self.request.get("edCodPostal1")
        paisCliente = self.request.get("edPais1")
        contactoCliente = self.request.get("edContacto1")
        emailCliente = self.request.get("edEmail1")
        telefonoCliente = self.request.get("edTelefono1")
        concepto = self.request.get("edConcepto")
        precio = self.request.get("edPrecio")
        unidad = self.request.get("edUnidad")
        importe = self.request.get("edImporte")
        IVA = self.request.get("edIVA")
        importeTotal = self.request.get("edImporteTotal")


        if len(CIF.strip()) == 0:
            CIF = "Desconocido"
        if len(nombre.strip()) == 0:
            nombre = "Desconocido"
        if len(direccion.strip()) == 0:
            direccion = "Desconocido"
        if len(poblacion.strip()) == 0:
            poblacion = "Desconocido"
        if len(provincia.strip()) == 0:
            provincia = "Desconocido"
        if len(codPostal.strip()) == 0:
            codPostal = "Desconocido"
        if len(pais.strip()) == 0:
            pais = "Desconocido"
        if len(contacto.strip()) == 0:
            contacto = "Desconocido"
        if len(telefono.strip()) == 0:
            telefono = "Desconocido"
        if len(CIFCliente.strip()) == 0:
            CIFCliente = "Desconocido"
        if len(nombreCliente.strip()) == 0:
            nombreCliente = "Desconocido"
        if len(direccionCliente.strip()) == 0:
            direccionCliente = "Desconocido"
        if len(poblacionCliente.strip()) == 0:
            poblacionCliente = "Desconocido"
        if len(provinciaCliente.strip()) == 0:
            provinciaCliente = "Desconocido"
        if len(codPostalCliente.strip()) == 0:
            codPostalCliente = "Desconocido"
        if len(paisCliente.strip()) == 0:
            paisCliente = "Desconocido"
        if len(contactoCliente.strip()) == 0:
            contactoCliente = "Desconocido"
        if len(emailCliente.strip()) == 0:
            emailCliente = "Desconocido"
        if len(telefonoCliente.strip()) == 0:
            telefonoCliente = "Desconocido"
        if len(concepto.strip()) == 0:
            concepto = "Desconocido"
        if len(precio.strip()) == 0:
            precio = "Desconocido"
        if len(unidad.strip()) == 0:
            unidad = "Desconocido"
        if len(importe.strip()) == 0:
            importe = "Desconocido"
        if len(IVA.strip()) == 0:
            IVA = "Desconocido"
        if len(importeTotal.strip()) == 0:
            importeTotal = "Desconocido"


        jinja = jinja2.get_jinja2(app=self.app)

        valores_plantilla = {
            "CIF": CIF,
            "nombre" : nombre,
            "direccion" : direccion,
            "poblacion" : poblacion,
            "provincia" : provincia,
            "codPostal" : codPostal,
            "pais" : pais,
            "contacto" : contacto,
            "telefono" : telefono,
            "CIFCliente": CIFCliente,
            "nombreCliente": nombreCliente,
            "direccionCliente": direccionCliente,
            "poblacionCliente": poblacionCliente,
            "provinciaCliente": provinciaCliente,
            "codPostalCliente": codPostalCliente,
            "paisCliente": paisCliente,
            "contactoCliente": contactoCliente,
            "emailCliente": emailCliente,
            "telefonoCliente" : telefonoCliente,
            "concepto": concepto,
            "precio": precio,
            "unidad": unidad,
            "importe": importe,
            "IVA": IVA,
            "importeTotal": importeTotal

        }
        self.response.write(jinja.render_template("answer.html", **valores_plantilla))

app = webapp2.WSGIApplication([
    ('/facturas', MainHandler)
], debug=True)
