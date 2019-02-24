# Python APIs and Datastores

![Let's avoid slides](https://assets.rbl.ms/17493360/980x.png)

## Goals
- Empowerment 
  - In Soviet Russia, your data is in charge of you
  - With Python, you are in charge of your data 
- Be comfortable asking questions about how to access your data
- Give a broad survey of what is possible and enough concepts so you can dig into whatever might be applicable to your environment
- Think of software development in three stages: get it working, get it working right, get it working quickly
  - Here, we focus on making it possible to _get it working_ by providing samples of different methods of data access
  - Learn concepts that enable asking more informed questions when you undertake a data project
- Awareness that **A beginning is a very delicate time** - _Dune, Frank Herbert_ 
  - Two phases of a software process to consider: development and operations
  - How you think about accessing your data influences the rest of your project
  - Be comfortable as you develop, but don't forget you might need to live with what you wrote for a while


## What is a Datastore?
- Where data is stored, organized, and persisted... what does this mean?
- Method for abstracting _storage details_ from your application
  - lots of different concerns/use cases result in lots of different ways to read and write data
- Does this matter? yes and no... if you're reading data, there are some things you might care about:
  - Where it comes from
  - What its _shape_ is
  - Performance/storage
#### Datastore Examples
  - Files (stored in formats - e.g. CSV, XML, JSON, binary, etc. - see below)
  - SQL databases
  - No-SQL databases
  - API


## What is an API?
- API == Application Programming Interface
- A way for a program (application) to talk to another program programmatically
#### Types of APIs
  - Memory based (e.g programs importing logic/capabilities from other programs)
    - importing libraries
    - talking to the operating system
  - Network/protocols (difference between protocol and API... we'll pretend there are none for the sake of this
    discussion, but I'm happy to discuss more offline)
    - standard protocols (e.g. HTTP, ODBC, FTP, etc.)
  - Custom formats accessed via networking protocols
    - typically data you might get over the Internet for a certain dataset or website, tailored for accessing that content
    - this brings us to data formats (which applies to files as well)
  - Web pages (plug for web scraping)


## Data Formats
- Assumes you have access to your _pile_ of data
- Formats are how you turn that _pile_ of bytes into something intelligible
  - [CSV (comma-separated values)](https://en.wikipedia.org/wiki/Comma-separated_values)
  - [JSON (Javascript Object Notation)](https://en.wikipedia.org/wiki/JSON)
  - [XML (eXtensible Markup Language)](https://en.wikipedia.org/wiki/XML)
  - [XLS/XLSX](https://en.wikipedia.org/wiki/Microsoft_Excel#File_formats)
  - [Binary](https://en.wikipedia.org/wiki/Binary_file)
  - Roll your own
- Based on data format, you may want some form of library to consume it


## Code, please
### Sanity check
- [derp.py](derp.py)
### Source examples
- [csv_examples.py](csv_examples.py)
- [xlsx_examples.py](xlsx_examples.py)
- [db_examples.py](db_examples.py)
- [api_examples.py](api_examples.py)
- [zip_examples.py](zip_examples.py)
### Put it all together
- [datamunge.py](datamunge.py)

