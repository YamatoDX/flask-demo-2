const END_POINT = "https://enigmatic-cove-02207.herokuapp.com/getGraph";
import NextCors from "nextjs-cors";
import { NextApiRequest, NextApiResponse } from "next";
import axios from "axios";

export default async function (req: NextApiRequest, res: NextApiResponse) {
    const { start, end, increment, inputFunction } = req.body;
    try {
        if (req.method !== "POST") {
            throw new Error("Must be a POST request");
        }
        if (!start || !end || !increment || !inputFunction) {
            throw new Error("Some Fields are missing!");
        }
        await NextCors(req, res, {
            methods: ["GET", "HEAD", "PUT", "PATCH", "POST", "DELETE"],
            origin: "*",
            optionsSuccessStatus: 200
        });
        const config = {
            headers: {
                "Content-Type": "application/json"
            }
        };
        console.log("req.body", req.body);
        const imageData = (
            await axios.post(END_POINT, JSON.stringify(req.body), config)
        ).data;
        return res.status(200).json({
            finalData: imageData,
            message: "ok!"
        });
    } catch (err) {
        console.error("Error in API", err);
        return res.status(400).json({
            message: err.message,
            status: "failed",
            finalData: ""
        });
    }
}
