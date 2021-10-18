import json
import requests
import boto3
from botocore.exceptions import ClientError
from dbc import DBC

def test_send(generatedLink, email):

    FILE_START = """
        <!DOCTYPE html>
            <html>
            <head>

            <meta charset="utf-8">
            <meta http-equiv="x-ua-compatible" content="ie=edge">
            <title>Email Confirmation</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
        
            """
    CSS = """
            <style type="text/css">
            /**
            * Google webfonts. Recommended to include the .woff version for cross-client compatibility.
            */
            @media screen {
                @font-face {
                font-family: 'Source Sans Pro';
                font-style: normal;
                font-weight: 400;
                src: local('Source Sans Pro Regular'), local('SourceSansPro-Regular'), url(https://fonts.gstatic.com/s/sourcesanspro/v10/ODelI1aHBYDBqgeIAH2zlBM0YzuT7MdOe03otPbuUS0.woff) format('woff');
                }

                @font-face {
                font-family: 'Source Sans Pro';
                font-style: normal;
                font-weight: 700;
                src: local('Source Sans Pro Bold'), local('SourceSansPro-Bold'), url(https://fonts.gstatic.com/s/sourcesanspro/v10/toadOcfmlt9b38dHJxOBGFkQc6VGVFSmCnC_l7QZG60.woff) format('woff');
                }
            }

            /**
            * Avoid browser level font resizing.
            * 1. Windows Mobile
            * 2. iOS / OSX
            */
            body,
            table,
            td,
            a {
                -ms-text-size-adjust: 100%; /* 1 */
                -webkit-text-size-adjust: 100%; /* 2 */
            }

            /**
            * Remove extra space added to tables and cells in Outlook.
            */
            table,
            td {
                mso-table-rspace: 0pt;
                mso-table-lspace: 0pt;
            }

            /**
            * Better fluid images in Internet Explorer.
            */
            img {
                -ms-interpolation-mode: bicubic;
            }

            /**
            * Remove blue links for iOS devices.
            */
            a[x-apple-data-detectors] {
                font-family: inherit !important;
                font-size: inherit !important;
                font-weight: inherit !important;
                line-height: inherit !important;
                color: inherit !important;
                text-decoration: none !important;
            }

            /**
            * Fix centering issues in Android 4.4.
            */
            div[style*="margin: 16px 0;"] {
                margin: 0 !important;
            }

            body {
                width: 100% !important;
                height: 100% !important;
                padding: 0 !important;
                margin: 0 !important;
            }

            /**
            * Collapse table borders to avoid space between cells.
            */
            table {
                border-collapse: collapse !important;
            }

            a {
                color: #1a82e2;
            }

            img {
                height: auto;
                line-height: 100%;
                text-decoration: none;
                border: 0;
                outline: none;
            }
            </style>
    
    
        </head>
    
        """
    BODY = """
        <body style="background-color: #e9ecef;">

        <!-- start body -->
            <table border="0" cellpadding="0" cellspacing="0" width="100%">

                <!-- start hero -->
                <tr>
                <td align="center" bgcolor="#e9ecef">
                    <table border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width: 600px;">
                    <tr>
                        <td align="left" bgcolor="#ffffff" style="padding: 36px 24px 0; font-family: 'Source Sans Pro', Helvetica, Arial, sans-serif; border-top: 3px solid #d4dadf;">
                        <h1 style="margin: 0; font-size: 32px; font-weight: 700; letter-spacing: -1px; line-height: 48px;">Confirma tu correo electrónico</h1>
                        </td>
                    </tr>
                    </table>
                </td>
                </tr>
                <!-- end hero -->

                <!-- start copy block -->
                <tr>
                <td align="center" bgcolor="#e9ecef">
                    <table border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width: 600px;">

                    <!-- start copy -->
                    <tr>
                        <td align="left" bgcolor="#ffffff" style="padding: 24px; font-family: 'Source Sans Pro', Helvetica, Arial, sans-serif; font-size: 16px; line-height: 24px;">
                        <p style="margin: 0;">Presiona el boton para confirmar la cuenta. Si no creaste una cuenta con el BancoDeTiempo, puedes eliminar este correo con gusto.</p>
                        </td>
                    </tr>
                    <!-- end copy -->

                    <!-- start button -->
                    <tr>
                        <td align="left" bgcolor="#ffffff">
                        <table border="0" cellpadding="0" cellspacing="0" width="100%">
                            <tr>
                            <td align="center" bgcolor="#ffffff" style="padding: 12px;">
                                <table border="0" cellpadding="0" cellspacing="0">
                                <tr>
                                    <td align="center" bgcolor="#1a82e2" style="border-radius: 6px;">
            """

    BUTTON = f"""
                                    <a href="{generatedLink}" target="_blank" style="display: inline-block; padding: 16px 36px; font-family: 'Source Sans Pro', Helvetica, Arial, sans-serif; font-size: 16px; color: #ffffff; text-decoration: none; border-radius: 6px;">Confirmar correo electrónico</a>
            """
    BODY2 = """
                                    </td>
                                </tr>
                                </table>
                            </td>
                            </tr>
                        </table>
                        </td>
                    </tr>
                    <!-- end button -->

                    <!-- start copy -->
                    <tr>
                        <td align="left" bgcolor="#ffffff" style="padding: 24px; font-family: 'Source Sans Pro', Helvetica, Arial, sans-serif; font-size: 16px; line-height: 24px;">
                        <p style="margin: 0;">Si el botón no funciona, favor de hacer clic al siguiente hipervínculo:</p>
            """
    LINK = f"""
                        <p style="margin: 0;"><a href="{generatedLink}" target="_blank">{generatedLink}</a></p>
            """
    BODY3 = """
                        </td>
                    </tr>
                    <!-- end copy -->

                    </table>
                </td>
                </tr>
                <!-- end copy block -->

            </table>
        <!-- end body -->

        </body>
        </html>
    
    
        """
    # Replace sender@example.com with your "From" address.
    # This address must be verified with Amazon SES.
    SENDER = "Banco De Tiempo <owoscarmetodoscomputacionales@gmail.com>"

    # Replace recipient@example.com with a "To" address. If your account 
    # is still in the sandbox, this address must be verified.
    RECIPIENT = email

    # If necessary, replace us-west-2 with the AWS Region you're using for Amazon SES.
    AWS_REGION = "us-east-1"

    # The subject line for the email.
    SUBJECT = "Confirma tu correo electrónico <Banco De Tiempo>"

    # The email body for recipients with non-HTML email clients.
    BODY_TEXT = ("Banco de Tiempo confirmation")
                
    # The HTML body of the email.
    BODY_HTML = FILE_START + CSS + BODY + BUTTON + BODY2 + LINK + BODY3           

    # The character encoding for the email.
    CHARSET = "UTF-8"

    # Create a new SES resource and specify a region.
    client = boto3.client('ses',region_name=AWS_REGION)

    # Try to send the email.
    try:
        #Provide the contents of the email.
        response = client.send_email(
            Destination={
                'ToAddresses': [
                    RECIPIENT,
                ],
            },
            Message={
                'Body': {
                    'Html': {
                        'Charset': CHARSET,
                        'Data': BODY_HTML,
                    },
                    'Text': {
                        'Charset': CHARSET,
                        'Data': BODY_TEXT,
                    },
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': SUBJECT,
                },
            },
            Source=SENDER,
            # If you are not using a configuration set, comment or delete the
            # following line
            #ConfigurationSetName=CONFIGURATION_SET,
        )
    # Display an error if something goes wrong.	
    except ClientError as e:
        return {
                "registerApproval":0,
                "error": "Error al enviar correo"
        }
        # (e.response['Error']['Message'])

def error_processor(error, idUsuario,correo):
    errorList ={
                idUsuario: "Usuario duplicado",
                correo: "Correo duplicado",
                "None": ""
                }
    errorMessage = "Error not found in list"
    try:
        error.index(idUsuario)
        errorMessage = errorList[idUsuario]
        secondVerification = False
    except:
        secondVerification = True
    
    if secondVerification:
        try:
            error.index(correo)
            errorMessage = errorList[correo]
        except:
            errorMessage = errorList["None"]

    return errorMessage

def approve_register(data):
    
    dbHandler = DBC()
    dbHandler.SQL_initialize()

    query = f"""INSERT INTO Usuario VALUES(
                        \"{data['idUsuario']}\",
                        \"{data['nombre']}\",
                        \"{data['apellidoP']}\",
                        \"{data['apellidoM']}\",
                        \"{data['calle']}\",
                        \"{data['numero']}\",
                        \"{data['colonia']}\",
                        \"{data['municipio']}\",
                        \"{data['estado']}\",
                        \"{data['correo']}\",
                        {data['CPP']},
                        \"{data['contrasena']}\",
                        0,
                        "NULL",
                        0,
                        0
                )   
                """

    query2 = f"""INSERT INTO Documentos VALUES(
                        \"{data['idUsuario']}\",
                        "NULL",
                        0,
                        "NULL",
                        0,
                        "NULL",
                        0
                )
                """

    queryResult, error = dbHandler.SQL_execute_oneway_statement(query)
    if not queryResult:
        error = error_processor(error, data['idUsuario'],data['correo'])
        data = {
            "registerApproval": 0,
            "error": error
            }
    else:
        queryResult2, error2 = dbHandler.SQL_execute_oneway_statement(query2)
        if not queryResult2:
            data = {
                "registerApproval": 0,
                "error": error2
                }
        else:
            data = {
                "registerApproval": 1,
                "error": ""
                }


    dbHandler.SQL_stop()
    
    return data
    
    #return 1

def generate_new_link(username):
    keys = {'a': 'u', 'b': 'v', 'c': 'w', 'd': 'x', 'e': 'y', 'f': 'z', 'g': 'a', 'h': 'b', 'i': 'c', 'j': 'd', 'k': 'e', 'l': 'f', 'm': 'g', 'n': 'h', 'o': 'i', 'p': 'j', 'q': 'k', 'r': 'l', 's': 'm', 't': 'n', 'u': 'o', 'v': 'p', 'w': 'q', 'x': 'r', 'y': 's', 'z': 't', 'A': 'U', 'B': 'V', 'C': 'W', 'D': 'X', 'E': 'Y', 'F': 'Z', 'G': 'A', 'H': 'B', 'I': 'C', 'J': 'D', 'K': 'E', 'L': 'F', 'M': 'G', 'N': 'H', 'O': 'I', 'P': 'J', 'Q': 'K', 'R': 'L', 'S': 'M', 'T': 'N', 'U': 'O', 'V': 'P', 'W': 'Q', 'X': 'R', 'Y': 'S', 'Z': 'T'}

    username = list(username)
    newUsername = []
    for letter in username:
        if letter in keys:
            newUsername.append(keys[letter])
        else:
            newUsername.append(letter)
    
    newUsername = "".join(newUsername)
    link = f"https://s4rnu8km1j.execute-api.us-east-1.amazonaws.com/verify/verifyuser?username={newUsername}"

    return link

def lambda_handler(event, context):
    
    image = event["image"]

    data = approve_register(event)

    callAPI = "https://bka70s5pka.execute-api.us-east-1.amazonaws.com/API/uploadimage"
    dataPhoto = {
        "image": image,
        "type": "ProfilePicture",
        "username": event["idUsuario"]
    }
    response = requests.post(callAPI, json.dumps(dataPhoto))
    response = json.loads(response.content)
    transactionApproval = response["transactionApproval"]

    if not transactionApproval:
        data["registerApproval"] = 0
        data["error"] = "Error submiting image"
    else:
        link = generate_new_link(event["idUsuario"])
        test_send(link, event["correo"])

    return data