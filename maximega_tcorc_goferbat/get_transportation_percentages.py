import urllib.request
import json
import dml
import prov.model
import datetime
import uuid
import pandas as pd

class get_transportation_percentages(dml.Algorithm):
    contributor = 'maximega_tcorc'
    reads = []
    writes = ['maximega_tcorc.transportation_percentages']

    @staticmethod
    def execute(trial = False):
        startTime = datetime.datetime.now()

        repo_name = get_transportation_percentages.writes[0]
        # ----------------- Set up the database connection -----------------
        client = dml.pymongo.MongoClient()
        repo = client.repo
        repo.authenticate('maximega_tcorc', 'maximega_tcorc')

        # ------------------ Data retrieval ---------------------
        url = 'http://datamechanics.io/data/maximega_tcorc/nta_public_transport_percentage.csv'
        data = pd.read_csv(url).to_json(orient = "records")
        json_response = json.loads(data)


        # ----------------- Data insertion into Mongodb ------------------
        repo.dropCollection('transportation_percentages')
        repo.createCollection('transportation_percentages')
        repo[repo_name].insert_many(json_response)
        repo[repo_name].metadata({'complete':True})
        print(repo[repo_name].metadata())
        
        repo.logout()

        endTime = datetime.datetime.now()

        return {"start":startTime, "end":endTime}

    @staticmethod
    def provenance(doc = prov.model.ProvDocument(), startTime = None, endTime = None):
        '''
            Create the provenance document describing everything happening
            in this script. Each run of the script will generate a new
            document describing that invocation event.
        '''

        # Set up the database connection.
        client = dml.pymongo.MongoClient()
        repo = client.repo
        repo.authenticate('maximega_tcorc', 'maximega_tcorc')
        doc.add_namespace('alg', 'http://datamechanics.io/algorithm/') # The scripts are in <folder>#<filename> format.
        doc.add_namespace('dat', 'http://datamechanics.io/data/') # The data sets are in <user>#<collection> format.
        doc.add_namespace('ont', 'http://datamechanics.io/ontology#') # 'Extension', 'DataResource', 'DataSet', 'Retrieval', 'Query', or 'Computation'.
        doc.add_namespace('log', 'http://datamechanics.io/log/') # The event log.
        #resources:
        doc.add_namespace('dmc', 'http://datamechanics.io/data/maximega_tcorc/')
        #agent
        this_script = doc.agent('alg:maximega_tcorc#get_transportation_percentages', {prov.model.PROV_TYPE:prov.model.PROV['SoftwareAgent'], 'ont:Extension':'py'})
        resource = doc.entity('dmc:nta_public_transport_percentage.csv', {'prov:label':'Percentage of Neighborhood commuters who take public transportation to work', prov.model.PROV_TYPE:'ont:DataResource', 'ont:Extension':'json'})
        
        get_transport_percentages = doc.activity('log:uuid'+str(uuid.uuid4()), startTime, endTime)

        doc.wasAssociatedWith(get_transport_percentages, this_script)
        doc.usage(get_transport_percentages, resource, startTime, None,
                  {prov.model.PROV_TYPE:'ont:Retrieval'
                  }
                  )
    
        transport_percentages = doc.entity('dat:maximega_tcorc#transportation_percentages', {prov.model.PROV_LABEL:'', prov.model.PROV_TYPE:'ont:DataSet'})
        doc.wasAttributedTo(transport_percentages, this_script)
        doc.wasGeneratedBy(transport_percentages, get_transport_percentages, endTime)
        doc.wasDerivedFrom(transport_percentages, resource, get_transport_percentages, get_transport_percentages, get_transport_percentages)

        repo.logout()
                
        return doc

