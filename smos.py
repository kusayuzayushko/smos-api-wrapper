import requests
from requests import Session

class SMOS:
    # Documentation https://api.simplemining.net/docs.html
    # to initiate an object:
    # import smos
    # from smos import SMOS
    # apikey = "api_1234...xyz"
    # smos = SMOS(apikey)
    # print(smos) 
    # should print an object
    #
    def __init__(self, token) -> None:
        self.apiurl = 'https://api.simplemining.net'
        self.headers = {'X-AUTH-TOKEN': token}
        self.session = Session()
        self.session.headers.update(self.headers)
    
    def getRigList(self, params={}):
        # https://api.simplemining.net/docs.html#tag/Rig/operation/getRigUserListCollection
        #
        # all get methods will return a json
        # 
        # usage example:
        # query={'status': 'off', 'itemsPerPage': '10'}
        # pp(smos.getRigList(query))
        #
        url = self.apiurl + '/rigs/user-list'
        r = self.session.get(url, params=params)
        data = r.json()
        return data
    
    def getFilterList(self, params={}):
        # https://api.simplemining.net/docs.html#tag/Rig/operation/getFilterListRigCollection
        # leaving params as an empty non required there for sonsistency with other methods
        url = self.apiurl + '/rigs/filter-list'
        r = self.session.get(url, params=params)
        data = r.json()
        return data
    
    def getRigsSummary(self, params={}):
        # https://api.simplemining.net/docs.html#tag/Rig/operation/getRigSummaryCollection
        url = self.apiurl + '/rigs/summary'
        r = self.session.get(url, params=params)
        data = r.json()
        return data
    
    def getRigDetailes(self, id, params={}):
        # https://api.simplemining.net/docs.html#tag/Rig/operation/getRigItem
        # leaving the possibility of setting id as a string or an integer there.
        # d = smos.getRigDetailes(1) or smos.getRigDetailes("1")
        # cos why not
        url = self.apiurl + '/rigs/' + str(id)
        r = self.session.get(url, params=params)
        data = r.json()
        return data
    
    def getRigConsole(self, id, params={}):
        # https://api.simplemining.net/docs.html#tag/Rig/operation/getConsoleRigItem
        url = self.apiurl + '/rigs/' + str(id) + '/console'
        r = self.session.get(url, params=params)
        data = r.json()
        return data
    
    def getDepositAddress(self, params):
        # https://api.simplemining.net/docs.html#tag/Deposit/operation/addressDepositCollection
        # currency = {'currency': 'eth'}
        # address = smos.getDepositAddress(currency)
        #
        url = self.apiurl + '/deposits/address'
        r = self.session.get(url, params=params)
        data = r.json()
        return data
    
    def getDepositSummary(self, params={}):
        # https://api.simplemining.net/docs.html#tag/Deposit/operation/summaryDepositCollection
        url = self.apiurl + '/deposits/summary'
        r = self.session.get(url, params=params)
        data = r.json()
        return data
        
    
    def getDepositList(self, params={}):
        # https://api.simplemining.net/docs.html#tag/Deposit/operation/userListDepositCollection
        # params = {'page': 1, 'itemsPerPage': '100', 'order[amountUsd]': 'asc'}
        # list = smos.getDepositList(params)
        #
        url = self.apiurl + '/deposits/user-list'
        r = self.session.get(url, params=params)
        data = r.json()
        return data
        
    def getAvailableCommands(self, params={}):
        #  https://api.simplemining.net/docs.html#tag/RigCommand/operation/getRigCommandCollection
        url = self.apiurl + '/rig-commands'
        r = self.session.get(url, params=params)
        data = r.json()
        return data
    
    def deleteRig(self, id):
        # https://api.simplemining.net/docs.html#tag/Rig/operation/deleteRigItem
        # all delete and patch methods will return status code
        # cos there is nothing useful in the response anyway
        #
        url = self.apiurl + '/rigs/' + str(id)
        r = self.session.delete(url)
        data = r.status_code 
        return data
    
    def executeReboot(self, params):
        # https://api.simplemining.net/docs.html#tag/Rig/operation/patchExecuteRebootCollection
        # params = '{"rigIds": [761897,111111,222222,987654]}'
        # reboot = smos.executeReboot(params)
        # >pp(reboot)
        # 200
        #
        url = self.apiurl + '/rigs/execute-reboot'
        r = self.session.patch(url, headers={'Content-Type': 'application/merge-patch+json'}, data=params)
        data = r.status_code
        return data
    
    def executeRestart(self, params):
        # https://api.simplemining.net/docs.html#tag/Rig/operation/patchExecuteReloadCollection
        url = self.apiurl + '/rigs/execute-reload'
        r = self.session.patch(url, headers={'Content-Type': 'application/merge-patch+json'}, data=params)
        data = r.status_code
        return data
    
    def executePause(self, params):
        # https://api.simplemining.net/docs.html#tag/Rig/operation/patchExecutePauseCollection
        url = self.apiurl + '/rigs/execute-pause'
        r = self.session.patch(url, headers={'Content-Type': 'application/merge-patch+json'}, data=params)
        data = r.status_code
        return data
    
    def executeResume(self, params):
        # https://api.simplemining.net/docs.html#tag/Rig/operation/patchExecuteResumeCollection
        url = self.apiurl + '/rigs/execute-resume'
        r = self.session.patch(url, headers={'Content-Type': 'application/merge-patch+json'}, data=params)
        data = r.status_code
        return data
    
    def executeFindRig(self, params):
        # https://api.simplemining.net/docs.html#tag/Rig/operation/patchExecuteRigDetectCollection
        url = self.apiurl + '/rigs/execute-rig-detect'
        r = self.session.patch(url, headers={'Content-Type': 'application/merge-patch+json'}, data=params)
        data = r.status_code
        return data

    def executeFindGPU(self, params):
        # https://api.simplemining.net/docs.html#tag/Rig/operation/patchExecuteRigGpuDetectCollection
        url = self.apiurl + '/rigs/execute-rig-gpu-detect'
        r = self.session.patch(url, headers={'Content-Type': 'application/merge-patch+json'}, data=params)
        data = r.status_code
        return data
    
    def executeShutdown(self, params):
        # https://api.simplemining.net/docs.html#tag/Rig/operation/patchExecuteShutdownCollection
        url = self.apiurl + '/rigs/execute-shutdown'
        r = self.session.patch(url, headers={'Content-Type': 'application/merge-patch+json'}, data=params)
        data = r.status_code
        return data
    
    def executeSleep(self, params):
        # https://api.simplemining.net/docs.html#tag/Rig/operation/patchExecuteSleepCollection
        url = self.apiurl + '/rigs/execute-sleep'
        r = self.session.patch(url, headers={'Content-Type': 'application/merge-patch+json'}, data=params)
        data = r.status_code
        return data
    
    def executeClearCounter(self, params):
        # https://api.simplemining.net/docs.html#tag/Rig/operation/patchExecuteClearCounterCollection
        url = self.apiurl + '/rigs/execute-clear-counter'
        r = self.session.patch(url, headers={'Content-Type': 'application/merge-patch+json'}, data=params)
        data = r.status_code
        return data
    
    def executeDelete(self, params):
        # https://api.simplemining.net/docs.html#tag/Rig/operation/patchExecuteDeleteCollection
        url = self.apiurl + '/rigs/execute-delete'
        r = self.session.patch(url, headers={'Content-Type': 'application/merge-patch+json'}, data=params)
        data = r.status_code
        return data
    
    def executeCommand(self, params):
        # https://api.simplemining.net/docs.html#tag/Rig/operation/patchExecuteCommandCollection
        url = self.apiurl + '/rigs/execute-command'
        r = self.session.patch(url, headers={'Content-Type': 'application/merge-patch+json'}, data=params)
        data = r.status_code
        return data


def main():
    print("")
    print("is not meant to be used as a script...")
    print("")
    # import secrets
    # from pprint import pprint as pp
    # smos = SMOS(secrets.api_key)
    # pp(smos)

if __name__ == '__main__':
    main()

