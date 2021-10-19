from dbc import DBC

def get_html_page(email):

    LINK = f"""
                    window.location.href = 'https://s4rnu8km1j.execute-api.us-east-1.amazonaws.com/verify/passwordrecovery?email={email}&data='+hashHex;
            """
    HTML = """

<!DOCTYPE html>
<html>

<head>

    <meta charset="utf-8">
    <meta http-equiv="x-ua-compatible" content="ie=edge">
    <title>Email Confirmation</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
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
            -ms-text-size-adjust: 100%;
            /* 1 */
            -webkit-text-size-adjust: 100%;
            /* 2 */
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
    """


    SCRIPT = """ 
    
    <script type="text/javascript">

        async function ChangePassword() {
            var password = document.getElementById("password").value;
            if((password.length >= 8) && (password.length<=40)){		
                var mayuscula = false;
                var minuscula = false;
                var numero = false;
                var caracter_raro = false;
                
                for(var i = 0;i<password.length;i++)
                {
                    if(password.charCodeAt(i) >= 65 && password.charCodeAt(i) <= 90)
                    {
                        mayuscula = true;
                    }
                    else if(password.charCodeAt(i) >= 97 && password.charCodeAt(i) <= 122)
                    {
                        minuscula = true;
                    }
                    else if(password.charCodeAt(i) >= 48 && password.charCodeAt(i) <= 57)
                    {
                        numero = true;
                    }
                    else
                    {
                        caracter_raro = true;
                    }
                }
                if(mayuscula != true || minuscula != true || caracter_raro != true || numero != true)
                {
                    alert("La contraseña debe contener por lo menos una letra Mayúscula, una Minúscula, un Número y un Caracter especial");
                    form_correct=false;
                }else{
                    const msgBuffer = new TextEncoder().encode(password);
                    // hash the message
                    const hashBuffer = await crypto.subtle.digest('SHA-256', msgBuffer);
                    // convert ArrayBuffer to Array
                    const hashArray = Array.from(new Uint8Array(hashBuffer));
                    // convert bytes to hex string                  
                    const hashHex = hashArray.map(b => ('00' + b.toString(16)).slice(-2)).join('');
    """

    HTML2 = """
                }

            }else{
                alert("La contraseña debe tener entre 8 y 30 caracteres");
            }


        }
    </script>
    </head>


    <body style="background-color: #e9ecef;">



        <!-- start body -->
        <table border="0" cellpadding="0" cellspacing="0" width="100%">

            <!-- start hero -->
            <tr>
                <td align="center" bgcolor="#e9ecef">
                    <table border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width: 600px;">
                        <tr>
                            <td align="left" bgcolor="#ffffff"
                                style="padding: 36px 24px 0; font-family: 'Source Sans Pro', Helvetica, Arial, sans-serif; border-top: 3px solid #d4dadf;">
                                <h1
                                    style="margin: 0; font-size: 32px; font-weight: 700; letter-spacing: -1px; line-height: 48px;">
                                    Ingresa tu nueva contraseña</h1>
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

                        <tr>
                            <td align="left" bgcolor="#ffffff">
                                <table border="0" cellpadding="0" cellspacing="0" width="100%">
                                    <tr>
                                        <td align="center" bgcolor="#ffffff" style="padding: 12px;">
                                            <table border="0" cellpadding="0" cellspacing="0">
                                                <tr bgcolor="#ffffff">
                                                    <td align="center" bgcolor="#ffffff" style="border-radius: 6px;">
                                                        <input
                                                        style="display: inline-block; padding: 16px 36px; font-family: 'Source Sans Pro', Helvetica, Arial, sans-serif; font-size: 16px; color: #ffffff; text-decoration: none; border-radius: 6px; color: black;"
                                                        id="password" type="text">
                                                        <!--|||||||||||||||| BOTON |||||||||||||||| -->

                                                        <button onclick="ChangePassword()"
                                                            style="display: inline-block; padding: 16px 36px; font-family: 'Source Sans Pro', Helvetica, Arial, sans-serif; font-size: 16px; background-color: #00BDFF; text-decoration: none; border-radius: 6px;">Cambiar
                                                            contraseña</button>
                                                        <!--|||||||||||||||| BOTON |||||||||||||||| -->

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

                    </table>
                </td>
            </tr>
            <!-- end copy block -->

        </table>
        <!-- end body -->

    </body>

    </html>    
    
    
    """
    HTML = HTML + SCRIPT + LINK +  HTML2

    return HTML

def update_password(email, password):

    dbHandler = DBC()
    dbHandler.SQL_initialize()

    query = f"UPDATE Usuario SET contrasena = \"{password}\" WHERE correo = \"{email}\" "
    queryResult = dbHandler.SQL_execute_oneway_statement(query)

    dbHandler.SQL_stop()

    if queryResult:
        return True
    return False


    pass


def change_password(email, password):



    transactionApproval = update_password(email, password)

    if transactionApproval:
        error = "Contraseña cambiada exitosamente"
    else:
        error = "Ocurrió un error al cambiar tu contraseña, por favor intentalo más tarde"

    HTML_FILE = """
<!DOCTYPE html>
<html>
<head>

  <meta charset="utf-8">
  <meta http-equiv="x-ua-compatible" content="ie=edge">
  <title>Email Confirmation</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
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
<body style="background-color: #e9ecef;">

  <!-- start body -->
  <table border="0" cellpadding="0" cellspacing="0" width="100%">

    <!-- start logo -->
    <tr>
      <td align="center" bgcolor="#e9ecef">
        <table border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width: 600px;">
          <tr>
            <td align="center" valign="top" style="padding: 36px 24px;">
              <a href="https://sendgrid.com" target="_blank" style="display: inline-block;">
                <img src="https://bancodetiempo.s3.amazonaws.com/logo.png" alt="Logo" border="0" width="48" style="display: block; width: 48px; max-width: 48px; min-width: 48px;">
              </a>
            </td>
          </tr>
        </table>
      </td>
    </tr>
    <!-- end logo -->


    <!-- start copy block -->
    <tr>
      <td align="center" bgcolor="#e9ecef">
        <table border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width: 600px;">

          <!-- start copy -->
          <tr>
            <td align="left" bgcolor="#ffffff" style="padding: 24px; font-family: 'Source Sans Pro', Helvetica, Arial, sans-serif; font-size: 16px; line-height: 24px;">

"""

    CONTENT_HTML_FILE = f"""
                        <h1 style="margin: 0; font-size: 32px; font-weight: 700; letter-spacing: -1px; line-height: 48px;">{error}</h1>
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

    HTML = HTML_FILE + CONTENT_HTML_FILE

    return HTML

def lambda_handler(event, context):
    # TODO implement
    email = event["queryStringParameters"]["email"]
    if "data" not in event["queryStringParameters"]:
        HTML = get_html_page(email)
    else:
        HTML = change_password(email,event["queryStringParameters"]["data"])
    
    return {
        'statusCode': 200,
        'body': HTML,
        "headers": {"Content-Type": "text/html"}
    }
