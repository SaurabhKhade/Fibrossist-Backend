def mail(data,otp):
    return f'''\
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Verify your account</title>
  </head>
  <body>
    <div
      style="
        font-family: Helvetica, Arial, sans-serif;
        width: 100%;
        overflow: auto;
        line-height: 2;
      "
    >
      <div style="margin: 50px auto; width: 70%; padding: 20px 0">
        <div style="border-bottom: 1px solid #eee">
          <a
            href=""
            style="
              font-size: 1.4em;
              color: #00466a;
              text-decoration: none;
              font-weight: 600;
            "
            >Fibrossist</a
          >
        </div>
        <p style="font-size: 1.1em">Hi, {data["name"]} {data["surname"]}</p>
        <p>
          Thank you for choosing Your Fibrossist. Click on the button given
          below to complete your Sign Up procedures. link is valid for 10
          minutes only.
        </p>
        <a
          href="fibrossit.com/verify-account?otp={otp}"
          style="text-decoration: none"
        >
          <h2
            style="
              background: #00466a;
              margin: 0 auto;
              width: max-content;
              padding: 0 10px;
              color: #fff;
              border-radius: 4px;
              cursor: pointer;
            "
          >
            verify
          </h2>
        </a>
        <p style="font-size: 0.9em">Regards,<br />Fibrossist</p>
        <hr style="border: none; border-top: 1px solid #eee" />
        <div
          style="
            float: right;
            padding: 8px 0;
            color: #aaa;
            font-size: 0.8em;
            line-height: 1;
            font-weight: 300;
          "
        >
          <p>Fibrossist System Inc</p>
          <a href="ibrossist.vercel.app" referrerpolicy="no-referrer">
            website</a
          >
        </div>
      </div>
    </div>
  </body>
</html>
'''