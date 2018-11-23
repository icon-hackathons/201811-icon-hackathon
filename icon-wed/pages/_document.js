import Document, { Head, Main, NextScript} from "next/document";

export default class MyDocument extends Document {
    render() {
        return (
            <html>
                <Head>
                    <meta charSet="utf-8"/>
                    <meta name="viewport" content="width=device-width, initial-scale=1"/>
                    <style jsx global>{`
                        body { margin: 0; color: #555; }
                        
                        .header { width: 100vw; height: 60px; top: 0; text-align: center}
                        .header > img { position: relative; display: inline-block; width: 45vw; bottom: -20px; }
                        
                        .footer { position: absolute; bottom: 0; width: 100%; height: 60px; line-height: 60px; }
                        .footer > span { background-color: blue; color: yellow; font-size: 5px; display: inline-block; width: 20%; text-align: center }
                        
                        .index { text-align: center; }
                        .index > p { position: relative; top: 30vh; display: inline-block; width: 65vw; font-size: 15px; }
                        .index > img { position: relative; top: 30vh; display: inline-block; width: 65vw; }
                        .index > .button-holder { position: absolute; bottom: 20vh; width: 100vw; height: 60px; text-align: center; }
                        .index > .button-holder > button { border-radius: 60px; display: inline-block; width: 300px; height: 60px; line-height: 60px; font-size: 17px; border: none; background-color: #0aafb3; color: #fff; }

                        .main { text-align: center; }
                        .main > p { position: relative; top: 15vh; display: inline-block; width: 65vw; font-size: 15px; }
                        .main > img { position: relative; top: 15vh; display: inline-block; width: 65vw; }
                        .main > .button-holder { position: absolute; bottom: 20vh; width: 100vw; height: 60px; text-align: center; }
                        .main > .button-holder > button { border-radius: 60px; display: inline-block; width: 300px; height: 60px; line-height: 60px; font-size: 17px; border: none; background-color: #0aafb3; color: #fff; }

                        .register { color: #575757; }
                        .register > div.title { text-align: center; height: 80px; line-height: 80px; font-size: 20px; }
                        .register > .content { height: calc(100% - 140px); display: inline-block; }
                        .register > .content > p { padding: 0 10px; font-size: 18px; }
                        .register > .content > table { padding: 0 20px; margin-bottom: 15px; }
                        .register > .content > table.last { margin-bottom: 40px; }
                        .register > .content tr > td:first-child { width: 65px; }
                        .register > .content tr > td > input { width: calc(100vw - 130px); }
                        .register > .content > div { padding: 0 20px; margin-top: 10px; }
                        .register > .content > div > textarea { margin-top: 5px; width: calc(100vw - 62px); height: 150px; }
                        .register > .content > hr { width: 75vw; margin-block: 40px; border: 0.5px solid #ddd; }
                        .register > .content > .button-holder { width: calc(100vw - 40px); height: 60px; text-align: center; margin-bottom: 40px; }
                        .register > .content > .button-holder > button { display: inline-block; }
                        .register > .content > p.caution { width: calc(100vw - 20px); text-align: center; font-size: 13px; color: red; display: inline-block; margin-bottom: 40px; }

                        .preview { text-align: center; color: #575757; }
                        .preview > div.title { height: 80px; line-height: 80px; font-size: 20px; }
                        .preview > .content { height: calc(100vh - 140px); display: inline-block; font-family: serif; }
                        .preview > .content > .separator { width: 40px; margin: 15px; }
                        .preview > .content > .separator.last { margin: 40px }
                        .preview > .content > .groom-bride { margin-bottom: 35px; }
                        .preview > .content > .groom-bride > p:first-child { font-size: 25px !important; }
                        .preview > .content > .groom-bride > p:last-child { font-weight: bold; }
                        .preview > .content > hr { width: 75vw; margin-block: 40px; border: 0.5px solid #ddd; }
                        .preview > .content > .father-mother { margin: 20px 0; }
                        .preview > .content > .father-mother > li:first-child { font-size: 18px; margin-bottom: 5px; }
                        .preview > .content > .father-mother > li:last-child { font-size: 15px; font-weight: bold; }
                        .preview > .content > .invitation-message { padding: 0 12.5vw; margin-bottom: 35px; }
                        .preview > .content > .invitation-message > p:first-child { font-size: 20px; }
                        .preview > .content > .invitation-message > p:last-child { white-space: pre-line; line-height: 1.5; }
                        .preview > .content > img { width: 100vw; }
                        .preview > .content > .wedding-information { padding: 0 12.5vw; }
                        .preview > .content > .wedding-information > p:first-child { font-size: 20px; }
                        .preview > .content > .wedding-information > table tr { text-align: left; font-size: 15px; }
                        .preview > .content > .wedding-information > table tr > td:first-child { font-weight: bold; width: 50px; }
                        .preview > .content > .button-holder { width: 100vw; height: 60px; text-align: center; margin-bottom: 40px; }
                        .preview > .content > .button-holder > button { display: inline-block; }
                        .preview > .content > .button-holder > button:first-child { margin-right: 20px; }

                        .preview > .content.invite { height: calc(100vh - 60px); display: inline-block; font-family: serif; }
                        .preview > .content.invite > .separator { margin-top: 40px; }
                        .preview > .content.invite > .button-holder > button { margin-right: 0; }

                        .complete { text-align: center; color: #575757; }
                        .complete > div.title { height: 80px; line-height: 80px; font-size: 20px; }
                        .complete > .content { height: calc(100vh - 140px); }
                        .complete > .content > img { width: 100vw; }
                        .complete > .content > .address { margin: 10px 0 20px 0; }
                        .complete > .content > .address > li:first-child { font-size: 18px; margin-bottom: 5px; }
                        .complete > .content > .address > li:last-child { font-size: 15px; font-weight: bold; color: #0aafb3; text-decoration: underline; }
                        .complete > .content > button { margin-top: 15px; display: inline-block; }
                        .complete > .content > hr { width: 75vw; margin-block: 40px; border: 0.5px solid #ddd; }
                        .complete > .content > hr.short-margin-top { margin-block-start: 20px; }
                        .complete > .content > .management > p { text-align: left; margin-left: 20px; font-size: 20px; }
                        .complete > .content > .management > table { width: 100vw; text-align: left; }
                        .complete > .content > .management > table tr:active { background-color: #eee; }
                        .complete > .content > .management > table tr > td:first-child { width: 80vw; padding: 20px; }

                        .check { text-align: center; color: #575757; }
                        .check > div.title { height: 80px; line-height: 80px; font-size: 20px; }
                        .check > .content { height: calc(100vh - 140px); display: inline-block; }
                        .check > .content > hr { width: 75vw; margin-block: 40px; border: 0.5px solid #ddd; }
                        .check > .content > .list > p { text-align: left; margin-left: 20px; font-size: 20px; }
                        .check > .content > .list > table.selector { table-layout: fixed; padding: 0 20px; width: 100vw; text-align: left;  }
                        .check > .content > .list > table.selector tr { text-align: left; font-size: 18px; }
                        .check > .content > .list > table.selector tr:first-child { margin-bottom: 10px; }
                        .check > .content > .list > table.selector tr > td { padding: 5px; }
                        .check > .content > .list > table.selector tr > td > span { width: 5px; height: 5px; display: inline-block; border-radius: 15px; border: 4px solid #0aafb3; }
                        .check > .content > .list > table.selector tr > td > span.on { background-color: white;}                
                        .check > .content > .list > table.selector tr > td > span.off { background-color: #0aafb3; opacity: 0.5; }
                        .check > .content > .list > table.data { table-layout: fixed; padding: 0; width: calc(100vw - 40px); margin: 0 20px; font-size: 15px; margin-top: 30px; border: 0.5px solid #ddd; }
                        .check > .content > .list > table.data th { border-bottom: 0.5px solid #ddd; }
                        .check > .content > .list > table.data th { padding: 10px; }
                        .check > .content > .list > table.data td { padding: 10px; }
                        .check > .content > .list > table.data > thead th:nth-child(2) { width: 60px; }
                        .check > .content > .list > table.data > thead th:nth-child(3) { width: 140px; }
                        .check > .content > .list > table.data > tbody td:nth-child(3) { color: #0aafb3; text-decoration: underline; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
                        .check > .content > .dashboard { display: inline-block; width: 100vw; height: 250px; background-color: #0aafb3; }
                        .check > .content > .dashboard > p:first-child { font-weight: bold; font-size: 25px; color: #fff; margin-block: 0; margin-top: 20px; }
                        .check > .content > .dashboard > p:nth-child(2) { font-size: 15px; color: #fff; margin-block: 0; margin-bottom: 10px; }
                        .check > .content > .dashboard > div.count > span { font-size: 20px; line-height: 60px; display: inline-block; background-color: #fff; width: 60px; height: 60px; border-radius: 60px; }
                        .check > .content > .dashboard > div.count > span:not(:last-child) { margin-right: 10px; }
                        .check > .content > .dashboard > div.description > span { font-weight: bold; font-size: 13px; display: inline-block; color: #fff; width: 60px; margin-top: 10px; }
                        .check > .content > .dashboard > div.description > span:not(:last-child) { margin-right: 10px; }
                        .check > .content > .dashboard > div.buttons { display: inline-block; }
                        .check > .content > .dashboard > div.buttons > button { display: inline-block; background-color: #fff; color: #0aafb3; margin-top: 20px; }
                        .check > .content > .dashboard > div.buttons > button:not(:last-child) { margin-right: 10px; }

                        // 공통
                        .no-margin-bottom { margin-bottom: 0; }
                        .no-padding-bottom { padding-bottom: 0; }
                        textarea { resize: none; }
                        input, textarea { font-size: 15px; border: 0.5px solid #eee; padding: 10px; border-radius: 5px;  }
                        button:active { opacity: 0.5; }
                        ol, ul { list-style:none; margin-block: 0; padding-inline-start: 0px; }
                        table { border-spacing: 0; }
                        .content { height: calc(100vh - 60px); overflow-y: scroll; }
                        .content > p:first-child { margin-block-start: 0; }
                        .bottom-button { font-size: 17px; border: none; width: calc(100vw - 20px); margin: 10px; height: 60px; background-color: grey; }
                        button.long { border-radius: 60px; display: block; width: 300px; height: 60px; line-height: 60px; font-size: 17px; border: none; background-color: #0aafb3; color: #fff; }
                        button.short { border-radius: 60px; display: block; width: 150px; height: 60px; line-height: 60px; font-size: 17px; border: none; background-color: #0aafb3; color: #fff; }
                        button.slim { border-radius: 30px; display: block; width: 150px; height: 30px; line-height: 30px; font-size: 17px; border: none; background-color: #0aafb3; color: #fff; }
                        button.square { border-radius: 10px; display: inline-block; width: 80px; height: 80px; font-size: 17px; border: 1px solid #0aafb3; color: #0aafb3; background-color: #fff; }

                    `}</style>
                </Head>
                <body>                
                    <Main />
                    <NextScript />
                </body>
            </html>
        );
    }
}