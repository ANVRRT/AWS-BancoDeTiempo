from dbc import DBC
import json

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




def decrypt_username(username):
    keys = {'u': 'a', 'v': 'b', 'w': 'c', 'x': 'd', 'y': 'e', 'z': 'f', 'a': 'g', 'b': 'h', 'c': 'i', 'd': 'j', 'e': 'k', 'f': 'l', 'g': 'm', 'h': 'n', 'i': 'o', 'j': 'p', 'k': 'q', 'l': 'r', 'm': 's', 'n': 't', 'o': 'u', 'p': 'v', 'q': 'w', 'r': 'x', 's': 'y', 't': 'z', 'U': 'A', 'V': 'B', 'W': 'C', 'X': 'D', 'Y': 'E', 'Z': 'F', 'A': 'G', 'B': 'H', 'C': 'I', 'D': 'J', 'E': 'K', 'F': 'L', 'G': 'M', 'H': 'N', 'I': 'O', 'J': 'P', 'K': 'Q', 'L': 'R', 'M': 'S', 'N': 'T', 'O': 'U', 'P': 'V', 'Q': 'W', 'R': 'X', 'S': 'Y', 'T': 'Z'}
    username = list(username)
    newUsername = []
    for letter in username:
        if letter in keys:
            newUsername.append(keys[letter])
        else:
            newUsername.append(letter)
    
    return "".join(newUsername)

def verify_account(username):

    dbHandler = DBC()
    dbHandler.SQL_initialize()

    query = f"UPDATE Usuario SET email_approval = 1 WHERE idUsuario = \"{username}\" "
    queryResult = dbHandler.SQL_execute_oneway_statement(query)

    dbHandler.SQL_stop()
    if not queryResult:
        return 0
    
    return 1





def lambda_handler(event, context):
    # TODO implement
    username = event["queryStringParameters"]["username"]

    username = decrypt_username(username)

    result = verify_account(username)

    if result:
        error = "Correo electrónico confirmado exitosamente"
    else:
        error = "Algo salió mal, intenta verificarte más tarde"

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
    
    return {
        'statusCode': 200,
        'body': HTML,
        "headers": {"Content-Type": "text/html"}
    }
