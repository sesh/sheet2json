This is a blatant rip off* of [GSX2JSON](http://gsx2json.com/). Built during a few minutes of
downtime, and so that I could own the whole stack for a tiny side project.

Built with [Flask] & [Zappa] (and [requests], but everything is built with requests).

---

Usage example:

```bash
> http https://5dcia0j0vl.execute-api.ap-southeast-2.amazonaws.com/dev/<sheet_id>/<sheet_number>
```

Once a sheet is "published to web" use the id from the URL and the sheet number (1-indexed):

```
> http https://5dcia0j0vl.execute-api.ap-southeast-2.amazonaws.com/dev/1cH0PEHYheqDWrtFb-h0rTg0InY039YKEC8SmWQNntN0/1

{
    "rows": [
        {
            "faacategory": "Super",
            "icaocategory": "Heavy",
            "lrm": "",
            "mlwtons": "591.7",
            "mtowkg": "640,000",
            "torm": "3500",
            "type": "Antonov An-225"
        },
        {
            "faacategory": "Super",
            "icaocategory": "Heavy",
            "lrm": "",
            "mlwtons": "",
            "mtowkg": "589,670",
            "torm": "3660",
            "type": "Scaled Composites Model 351 Stratolaunch"
        },
        {
            "faacategory": "Super",
            "icaocategory": "Heavy",
            "lrm": "",
            "mlwtons": "427",
            "mtowkg": "589,670",
            "torm": "",
            "type": "Airbus A380-800F[1][2] (never built)"
        },
        {
            "faacategory": "Super",
            "icaocategory": "Heavy",
            "lrm": "1930",
            "mlwtons": "394",
            "mtowkg": "575,000",
            "torm": "3100",
            "type": "Airbus A380-800[2][3]"
        },
        ...
    ]
}
```

---

\* it's actually quite a bit worse, it only supports sheets with single-row headers
and doesn't have any error handling.

  [Flask]: http://flask.pocoo.org/
  [Zappa]: https://github.com/Miserlou/Zappa
  [requests]: https://requests.readthedocs.io/en/master/
