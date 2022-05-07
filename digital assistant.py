import wx,requests,bs4
import webbrowser
import wolframalpha as wfa
import wikipedia as wiki

class frame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,pos=wx.DefaultPosition,size=wx.Size(450,100),
                          style=wx.MINIMIZE_BOX|
                          wx.SYSTEM_MENU|
                          wx.CAPTION|
                          wx.CLOSE_BOX|
                          wx.CLIP_CHILDREN,
                          title="Digital_Assistant")
        panel=wx.Panel(self)
        sizer=wx.BoxSizer(wx.VERTICAL)
        tag=wx.StaticText(panel,label="hello I'am JARVIS.How can i help you")
        sizer.Add(tag,0,wx.ALL,5)
        self.text=wx.TextCtrl(panel,style=wx.TE_PROCESS_ENTER,size=(400,30))
        self.text.SetFocus()
        self.text.Bind(wx.EVT_TEXT_ENTER,self.OnFinish)
        sizer.Add(self.text,0,wx.ALL,5)
        panel.SetSizer(sizer)
        self.Show()

    def OnFinish(self,event):
        i=self.text.GetValue()
        i=i.lower()
        i=i.strip()
        ci=i
        x=i
        if i!="exit(0)":
                                try:
                                      app_id="9UR8K2-LLKTLAP53X"
                                      client=wfa.Client(app_id)
                                      ans=client.query(i)
                                      answer=next(ans.results).text
                                      print(answer)    
                                      print("______________________________________________________________________________")
                                except StopIteration:
                                      print(wiki.summary(i, sentences=3))
                                      print("______________________________________________________________________________")
                                except StopIteration:
                                    res=requests.get('https://google.com/search?q='+' '.join(x))
                                    s=bs4.BeautifulSoup(res.text,"html.parser")
                                    links=s.select('.r a')
                                    linksopen=min(4,len(links))
                                    for i in range(linksopen):
                                        webbrowser.open('https://google.com'+links[i].get('href'))
                                    print("______________________________________________________________________________")
                                except:
                                    print("No internet connectivity....or",end=" ")
                                    print("No record found....")
                                    print("______________________________________________________________________________")
        else:
            print("virtual assistant teriminated...")
            self.Destroy()
            exit(0)
        
app=wx.App()
f=frame()
f.Show()
app.MainLoop()
