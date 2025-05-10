import tkinter as tk


class Medical_App(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        self.master.geometry("1000x600")

        self.aLbl = tk.Label(self.master,text = '||||||||',bg="chocolate1", fg="black", width="1000",height="1", font=('Times New Roman',14))#DeepPink3
        self.aLbl.pack(side="bottom")

        self.photo = tk.PhotoImage(file="coronry.png")
        self.label = tk.Label(self.master, compound=tk.TOP, width=1500, height=700, image=self.photo, bg="white")
        self.label.image = self.photo
        self.label.pack(side=tk.LEFT, padx=2, pady=2, anchor="center")

        self.master.title("Coronary Heart Disease Medical Software")
        self.frame = tk.Frame(self.master)

        menubar = tk.Menu(self.master)
        self.master.config(menu=menubar)

        menu3 = tk.Menu(menubar, tearoff=0)
        #menu4 = tk.Menu(menubar, tearoff=0)
        edit_m = tk.Menu(menubar, tearoff=0)
        filemenu = tk.Menu(menubar, tearoff=0)
        anothermenu = tk.Menu(menubar, tearoff=0)
        menu2 = tk.Menu(menubar, tearoff=0)
        menu1 = tk.Menu(menubar, tearoff=0)

        menubar.add_cascade(label=" Patient ", menu=anothermenu, underline=0)
        menubar.add_cascade(label=" Causes ", menu=edit_m, underline=0)
        menubar.add_cascade(label=" Clinical ", menu=menu3, underline=0)
        menubar.add_cascade(label=" Pharmacy ", menu=filemenu, underline=0)
        menubar.add_cascade(label="Therapy", menu=menu2, underline=0)
        #menubar.add_cascade(label="State", menu=menu4, underline=0)
        menubar.add_cascade(label=" Doctor ", menu=menu1, underline=0)

        anothermenu.add_command(label="Diagnosis", command=self.nw_window)
        anothermenu.add_command(label="Treatment", command=self.nwindow)
        anothermenu.add_separator()
        anothermenu.add_command(label="Exit", command=self.onExit)

        menu3.add_command(label="Prevention", command=self.n_window)
        menu3.add_command(label="Symptoms of CHD", command=self.a_window)
        menu3.add_separator()
        #menu4.add_command(label="Medical Technology", command=self.mywindow)
        menu2.add_command(label="Contraindicated Procedures", command=self.cp_window)
        #menu4.add_separator()
        #filemenu.add_separator()
        filemenu.add_command(label="Drugs", command=self.com__window)
        menu1.add_command(label="Prescription", command=self.com_window)

        edit_m.add_command(label="Causes of CHD", command=self.newindow)
        #edit_m.add_command(label="Healing CHD", command=self.nwwindow)
        #edit_m.add_separator()
        #edit_m.add_cascade(label="Causes", menu=sub_menu, underline=0)

        #sub_menu.add_command(label="Causes of CHD", command = self.CHD__window)
     

    def n_window(self):
        self.n_window = tk.Toplevel(self.master)
        self.app = description(self.n_window)

    def a_window(self):
        self.a_window = tk.Toplevel(self.master)
        self.app = effects(self.a_window)

    def nw_window(self):
        self.nw_window = tk.Toplevel(self.master)
        self.app = diagnosis(self.nw_window)

    def nwindow(self):
        self.nwindow = tk.Toplevel(self.master)
        self.app = Treatment(self.nwindow)

    def cp_window(self):
        self.mywindow = tk.Toplevel(self.master)
        self.app = C_Procedure(self.mywindow)

    def newindow(self):
        self.newindow = tk.Toplevel(self.master)
        self.app = Causes(self.newindow)


    def com_window(self):
        self.com_window = tk.Toplevel(self.master)
        self.app = prescription(self.com_window)

    def com__window(self):
        self.com__window = tk.Toplevel(self.master)
        self.app = pharmacy(self.com__window)

#    def CHD__window(self):
 #       self.mywindow = tk.Toplevel(self.master)
  #      self.app = Causes(self.mywindow)


    def onExit(self):
        self.master.destroy()       # quit the entire application.


class description():
    def __init__(self, Apps):
        self.Apps = Apps
        self.frame = tk.Frame(self.Apps)
        self.Apps.geometry("1225x700")
        self.Apps.tk.call('wm', 'iconphoto', Apps._w, tk.PhotoImage(file='coronry_icon.png'))
        #self.Apps.title("Available Courses")
        self.Lbl = tk.Label(self.Apps, text = 'Medical DESCRIPTION', bg="chocolate1", fg='white', width="600", height="2")
        self.Lbl.pack(side='top')

        self.txt = tk.Text(self.Apps, height=50, width=100)
        self.txt.pack(side='left', expand='yes', fill='both')
        self.scroll = tk.Scrollbar(self.Apps, orient=tk.VERTICAL)
        self.scroll.config(command=self.txt.yview)
        self.txt.config(yscrollcommand=self.scroll.set)
        self.txt.config(font=('Times New Roman', 14))
        self.scroll.pack(side='right', ipady=330)

        outline = """
    There are several ways you can reduce your risk of developing coronary heart disease (CHD), such as lowering your blood pressure
    and cholesterol levels. Eat a healthy, balanced diet
    A low-fat, high-fibre diet is recommended, which should include plenty of fresh fruit and vegetables (5 portions a day) and whole grains.

    You should limit the amount of salt you eat to no more than 6g (0.2oz) a day as too much salt will increase your blood pressure.
    6g of salt is about 1 teaspoonful.

    There are 2 types of fat: saturated and unsaturated. You should avoid food containing saturated fats, because these will increase the
    levels of bad cholesterol in your blood.

    Foods high in saturated fat include:

    1.  meat pies
    2.  sausages and fatty cuts of meat
    3.  butter
    4.  ghee – a type of butter often used in Indian cooking
    5.  lard
    6.  cream
    7.  hard cheese
    8.  cakes and biscuits
    9.  foods that contain coconut or palm oil
    
    However, a balanced diet should still include unsaturated fats, which have been shown to increase levels of good cholesterol and help
    reduce any blockage in your arteries.

    Foods high in unsaturated fat include:

    1.  oily fish
    2.  avocados
    3.  nuts and seeds
    4.  sunflower, rapeseed, olive and vegetable oils

    You should also try to avoid too much sugar in your diet, as this can increase your chances of developing diabetes, which is proven to
    significantly increase your chances of developing CHD eating less saturated fat the facts about sugar

    Be more physically active Combining a healthy diet with regular exercise is the best way of maintaining a healthy weight.
    Having a healthy weight reduces your chances of developing high blood pressure.

    Regular exercise will make your heart and blood circulatory system more efficient, lower your cholesterol level, and also keep your blood
    pressure at a healthy level. Exercising regularly reduces your risk of having a heart attack. The heart is a muscle and, like any other muscle,
    benefits from exercise. A strong heart can pump more blood around your body with less effort.

    Any aerobic exercise, such as walking, swimming and dancing, makes your heart work harder and keeps it healthy. Keep to a healthy weight
    A GP or practice nurse can tell you what your ideal weight is in relation to your height and build. Alternatively, find out what your body
    mass index (BMI) is by using our BMI calculator. Give up smoking. If you smoke, giving up will reduce your risk of developing CHD.

    Smoking is a major risk factor for developing atherosclerosis (furring of the arteries). It also causes the majority of cases of coronary
    thrombosis in people under the age of 50.

    Research has shown you're up to 3 times more likely to successfully give up smoking if you use NHS support together with stop-smoking medicines,
    such as patches or gum.

    Ask a doctor about this or visit NHS Smoke free.
    Reduce your alcohol consumption
    If you drink, do not exceed the maximum recommended limits. men and women are advised not to regularly drink more than 14 units a week
    spread your drinking over 3 days or more if you drink as much as 14 units a week
    Always avoid binge drinking, as this increases the risk of a heart attack.

    Keep your blood pressure under control
    You can keep your blood pressure under control by eating a healthy diet low in saturated fat, exercising regularly and, if needed, taking
    medicine to lower your blood pressure. Your target blood pressure should be below 140/90mmHg. If you have high blood pressure, ask a GP to
    check your blood pressure regularly.

    Keep your diabetes under control
    You have a greater chance of developing CHD if you have diabetes. Being physically active and controlling your weight and blood pressure
    will help manage your blood sugar level.

    If you have diabetes, your target blood pressure level should be below 130/80mmHg.
    Take any prescribed medicine
    If you have CHD, you may be prescribed medicine to help relieve your symptoms and stop further problems developing.

    If you do not have CHD but have high cholesterol, high blood pressure or a history of family heart disease, your doctor may prescribe
    medicine to prevent you developing heart-related problems.

    If you're prescribed medicine, it's vital you take it and follow the correct dosage. Do not stop taking your medicine without consulting a
    doctor first, as doing so is likely to make your symptoms worse and put your health at risk.
                                                                          
                  """
        self.txt.insert(tk.END, outline)


    

class C_Procedure():
    def __init__(self, Apps):
        self.Apps = Apps
        self.frame = tk.Frame(self.Apps)
        self.Apps.geometry("1225x700")
        self.Apps.tk.call('wm', 'iconphoto', Apps._w, tk.PhotoImage(file='coronry_icon.png'))
        #self.Apps.title("Available Courses")
        self.Lbl = tk.Label(self.Apps, text = 'MEDICAL PROCEDURE', bg="chocolate1", fg='white', width="600", height="2")
        self.Lbl.pack(side='top')

        self.txt = tk.Text(self.Apps, height=50, width=100)
        self.txt.pack(side='left', expand='yes', fill='both')
        self.scroll = tk.Scrollbar(self.Apps, orient=tk.VERTICAL)
        self.scroll.config(command=self.txt.yview)
        self.txt.config(yscrollcommand=self.scroll.set)
        self.txt.config(font=('Times New Roman', 16))
        self.scroll.pack(side='right', ipady=330)

        outline = """
        
                                                Common medical procedures for heart conditions
    Once your doctor knows what your heart condition is, he or she will then decide what treatments or procedures you may need.

    Some of these procedures and treatments are explained below.

    Coronary angioplasty and stent implantation
    Coronary angioplasty is a procedure that helps to improve blood flow to your heart.

    A small balloon is inflated inside one or more of your coronary arteries to open up an area that has become very clogged and, therefore, narrow.

    After this, a special expandable metal tube (a ‘stent’) is usually put into the artery, expanded, and left there to keep the artery open.

    There are two types of stents:

    bare metal stents (BMS)
    drug-eluting stents (DES).
    Coronary angioplasty is not a cure for coronary heart disease. It only treats the part of the coronary artery that has become very narrow.al

    Thrombolytic therapy
    Thrombolytic therapy is a treatment in which you are given medicines through a drip to dissolve a blood clot that is narrowing or blocking a
    coronary artery.

    This improves blood flow to your heart muscle and around your body.

    Coronary artery bypass graft surgery (CABG)
    Coronary artery bypass graft surgery is also called bypass surgery or ‘CABG’ (pronounced ‘cabbage’). In this operation a blood vessel is taken from
    your chest, leg or arm and attached (‘grafted’) to your coronary artery. This lets blood detour (‘bypass’) around a narrowing or blockage in this
    artery.

    During this operation, your surgeon will cut down the midline of your chest, through your breastbone, to reach your heart.

    Bypass surgery improves blood flow to your heart muscle and reduces angina.

    Artificial pacemaker surgery
    An artificial pacemaker is a small device that is put under the skin of your chest, below your collar bone. One or two wires connect the
    pacemaker to the chambers of your heart.

    A pacemaker makes small electrical currents that stimulate your heart muscle and help it pump regularly.

    A pacemaker’s battery can last up to 10 years. Your doctor can check the battery every year, and replace it when needed.

    Defibrillation
    Defibrillation helps to restore a normal heart rhythm when your heart stops beating properly during cardiac arrest.
    It may also be used to treat other heart rhythm problems (like if your heart beats too slowly or too fast).

    Paddles or pads are put on your chest. A regulated electrical current is applied to your heart to make it start beating regularly again.

    You may be given an implantable cardiac defibrillator (ICD). This small device is put into your chest and connected to your heart by one or more
    wire leads. It monitors your heart rhythm and corrects it if it beats too slowly, too fast or stops beating.

    Heart valve surgery
    Heart valve surgery fixes a damaged or faulty heart valve and helps your heart to pump blood properly.

    Your surgeon cuts down the midline of your chest, through your breastbone, to reach your heart.
    The faulty heart valve will then be repaired or replaced.

                 """
        self.txt.insert(tk.END, outline)
    
class effects():
    def __init__(self, Apps):
        self.Apps = Apps
        self.frame = tk.Frame(self.Apps)
        self.Apps.geometry("1225x700")
        self.Apps.tk.call('wm', 'iconphoto', Apps._w, tk.PhotoImage(file='coronry_icon.png'))
        #self.Apps.title("Available Courses")
        self.Lbl = tk.Label(self.Apps, text = 'SYMPTOMS OF CHD', bg="chocolate1", fg='white', width="600", height="2")
        self.Lbl.pack(side='top')

        self.txt = tk.Text(self.Apps, height=50, width=100)
        self.txt.pack(side='left', expand='yes', fill='both')
        self.scroll = tk.Scrollbar(self.Apps, orient=tk.VERTICAL)
        self.scroll.config(command=self.txt.yview)
        self.txt.config(yscrollcommand=self.scroll.set)
        self.txt.config(font=('Times New Roman', 16))
        self.scroll.pack(side='right', ipady=330)

        outline = """
        
    The most common symptoms of coronary heart disease (CHD) are chest pain (angina) and breathlessness.

    But some people may not have any symptoms before they're diagnosed.

    ANGINA

    If your coronary arteries become partially blocked, it can cause chest pain (angina). This can be a mild, uncomfortable feeling

    similar to indigestion. However, a severe angina attack can cause a painful feeling of heaviness or tightness, usually in the `

    centre of the chest, which may spread to the arms, neck, jaw, back or stomach.

    Angina is often triggered by physical activity or stressful situations. Symptoms usually pass in less than 10 minutes, and can be relieved

    by resting or using a nitrate tablet or spray.

    HEART ATTACK

    If your arteries become completely blocked, it can cause a heart attack (myocardial infarction).

    Heart attacks can permanently damage the heart muscle and, if not treated straight away, can be fatal.

    Although symptoms can vary, the discomfort or pain of a heart attack is usually similar to that of angina. However, it's often more severe and

    may happen when you're resting. During a heart attack, you may also have the following symptoms:

    pain in other parts of the body – it can feel as if the pain is travelling from your chest to your arms, jaw, neck, back or stomach

    lightheadedness, sweating, nausea, breathlessness.

    The symptoms of a heart attack can also be similar to indigestion. For example, they may include a feeling of heaviness in your chest,

    a stomach ache or heartburn. A heart attack can happen at any time, including while you're resting. If heart pains last longer than 15 minutes,

    it may be the start of a heart attack. Unlike angina, the symptoms of a heart attack are not usually relieved using a nitrate tablet or spray.

    A heart attack can sometimes happen without any symptoms. This is known as a silent myocardial infarction and is more common in older people

    and people with diabetes.

    HEART FAILURE

    Heart failure can also happen in people with CHD. The heart becomes too weak to pump blood around the body, which can cause fluid to build up in

    the lungs, making it increasingly difficult to breathe.

    Heart failure can happen suddenly (acute heart failure) or gradually, over time (chronic heart failure).

    What to do if someone has a heart attack

    When someone has a heart attack, a bystander – often a relative with no medical expertise – is usually the first on the scene.

    However, less than 1% of the population have attended an emergency life support course.

    Heart start (funded by the British Heart Foundation), British Red Cross and St John Ambulance can teach you how to help someone having a

    heart attack.        
                  """
        self.txt.insert(tk.END, outline)
  
class diagnosis():
    def __init__(self, Apps):
        self.Apps = Apps
        self.frame = tk.Frame(self.Apps)
        self.Apps.geometry("1225x700")
        self.Apps.tk.call('wm', 'iconphoto', Apps._w, tk.PhotoImage(file='coronry_icon.png'))
        #self.Apps.title("Available Courses")
        self.Lbl = tk.Label(self.Apps, text = 'DIAGNOSIS', bg="chocolate1", fg='white', width="600", height="2")
        self.Lbl.pack(side='top')

        self.txt = tk.Text(self.Apps, height=50, width=100)
        self.txt.pack(side='left', expand='yes', fill='both')
        self.scroll = tk.Scrollbar(self.Apps, orient=tk.VERTICAL)
        self.scroll.config(command=self.txt.yview)
        self.txt.config(yscrollcommand=self.scroll.set)
        self.txt.config(font=('Times New Roman', 16))
        self.scroll.pack(side='right', ipady=330)

        outline = """
        
    Coronary heart disease (CHD) is usually diagnosed after a risk assessment and some further tests.

    RISK ASSESSMENT

    If a GP thinks you may be at risk of CHD, they may do a risk assessment for cardiovascular disease, heart attack or stroke.

    This may be carried out as part of an NHS Health Check.

    The GP will:

    ask about your medical and family history

    check your blood pressure

    does a blood test to assess your cholesterol level?

    Before having the cholesterol test, you may be asked not to eat for 12 hours so there's no food in your body that could affect the result.

    The GP or practice nurse can carry out the blood test. A sample will be taken either using a needle and a syringe or by pricking your finger.

    The GP will also ask about your lifestyle, how much exercise you do and whether you smoke. All these factors will be considered as part of

    the diagnosis.

    FURTHER TESTS

    You may be referred for further tests to help confirm CHD. A number of different tests are used to diagnose heart-related problems, including:

    ELECTROCARDIOGRAM (ECG)

    1.   exercise stress tests
    2.   X-rays
    3.   echocardiogram
    4.   blood tests
    5.   coronary angiography
    6.   radionuclide tests
    7.   MRI scans
    8.   CT scans
    9.   Further information
    10.  British Heart Foundation: tests
    11.  Blood Pressure UK: medical tests for high blood pressure        
                  """
        self.txt.insert(tk.END, outline)

class Treatment():
    def __init__(self, Apps):
        self.Apps = Apps
        self.frame = tk.Frame(self.Apps)
        self.Apps.geometry("1225x700")
        self.Apps.tk.call('wm', 'iconphoto', Apps._w, tk.PhotoImage(file='coronry_icon.png'))
        #self.Apps.title("Available Courses")
        self.Lbl = tk.Label(self.Apps, text = 'TREATMENT OF CHD', bg="chocolate1", fg='white', width="600", height="2")
        self.Lbl.pack(side='top')

        self.txt = tk.Text(self.Apps, height=50, width=100)
        self.txt.pack(side='left', expand='yes', fill='both')
        self.scroll = tk.Scrollbar(self.Apps, orient=tk.VERTICAL)
        self.scroll.config(command=self.txt.yview)
        self.txt.config(yscrollcommand=self.scroll.set)
        self.txt.config(font=('Times New Roman', 16))
        self.scroll.pack(side='right', ipady=330)

        outline = """
        
    Treatment for coronary heart disease (CHD) can help manage the symptoms and reduce the risk of further problems.

    CHD can be managed effectively with a combination of lifestyle changes, medicine and, in some cases, surgery.

    With the right treatment, the symptoms of CHD can be reduced and the functioning of the heart improved.

    THINGS YOU CAN DO TO HELP WITH CORONARY HEART DISEASE (CHD)

    If you've been diagnosed with coronary heart disease, making simple lifestyle changes can reduce your risk of having further episodes.

    For example, stopping smoking after a heart attack quickly reduces your risk of having a heart attack in the future to near that of a

    non-smoker. Other lifestyle changes, such as eating more healthily and doing regular exercise, will also reduce your future risk of

    heart disease. exercise and fitness, healthy eating, stop smoking.

    MEDICINES

    Many different medicines are used to treat CHD. Usually they either aim to reduce blood pressure or widen your arteries.

    Some heart medicines have side effects, so it may take a while to find one that works for you. A GP or specialist will discuss the various

    options with you. Heart medicines should not be stopped suddenly without the advice of a doctor as there's a risk this may make your

    symptoms worse.

    BLOOD-THINNING MEDICINES

    Blood thinners are a type of medicine that can help reduce the risk of a heart attack by thinning your blood and preventing it clotting.

    COMMON BLOOD-THINNING MEDICINES INCLUDE:

    low-dose aspirin
    clopidogrel
    rivaroxaban
    ticagrelor
    prasugrel
    Statins
    If you have high cholesterol, cholesterol-lowering medicine called statins may be prescribed.

    Examples include:

    1.  atorvastatin
    2.  simvastatin
    3.  rosuvastatin
    4.  pravastatin
    Statins work by blocking the formation of cholesterol and increasing the number of low-density lipoprotein (LDL) receptors in the liver.

    This helps remove LDL cholesterol from your blood, which makes a heart attack less likely. 

    Not all statins are suitable for everyone, so you may need to try several different types until you find one that's suitable.

    BETA BLOCKERS

    Beta blockers, including atenolol, bisoprolol, metoprolol and nebivolol, are often used to prevent angina and treat high blood pressure.

    They work by blocking the effects of a particular hormone in the body, which slows down your heartbeat and improves blood flow.

    NITRATES

    Nitrates are used to widen your blood vessels. Doctors sometimes refer to nitrates as vasodilators.

    They're available in a variety of forms, including tablets, sprays and skin patches such as glyceryl trinitrate and isosorbide mononitrate.

    Nitrates work by relaxing your blood vessels, letting more blood pass through them. This lowers your blood pressure and relieves any heart

    pain you have. Nitrates can have some mild side effects, including headaches, dizziness and flushed skin.

    ANGIOTENSIN-CONVERTING ENZYME (ACE) INHIBITORS

    ACE inhibitors are commonly used to treat high blood pressure. Examples include ramipril and lisinopril.

    They block the activity of a hormone called angiotensin-2, which causes the blood vessels to narrow.

    As well as stopping the heart working so hard, ACE inhibitors improve the flow of blood around the body.

    Your blood pressure will be monitored while you're taking ACE inhibitors, and regular blood tests will be needed to check that your kidneys

    are working properly. Less than 1 in 100 people have problems with the blood supply to their kidneys (renal stenosis) as a result of taking

    ACE inhibitors.

    Side effects of ACE inhibitors can include a dry cough and dizziness.

    Angiotensin-2 receptor blockers (ARBs)

    Angiotensin-2 receptor blockers (ARBs) work in a similar way to ACE inhibitors.

    They're used to lower your blood pressure by blocking angiotensin-2.

    Mild dizziness is usually the only side effect. They're often prescribed as an alternative to ACE inhibitors, as they do not cause a dry cough.

    CALCIUM CHANNEL BLOCKERS

    Calcium channel blockers also work to decrease blood pressure by relaxing the muscles that make up the walls of your arteries.

    This causes the arteries to become wider, reducing your blood pressure.

    Examples include amlodipine, verapamil and diltiazem.

    Side effects include headaches and facial flushing, but these are mild and usually decrease over time.

    DIURETICS

    Sometimes known as water pills, diuretics work by flushing excess water and salt from the body through urine.

    PROCEDURES AND SURGERY

    If your blood vessels are narrow as the result of a build-up of atheroma (fatty deposits) or if your symptoms cannot be controlled using

    medicines, interventional procedures or surgery may be needed to open up or bypass blocked arteries.

    Here are some of the main procedures used to treat blocked arteries.

    CORONARY ANGIOPLASTY

    Coronary angioplasty is also known as percutaneous coronary intervention (PCI), percutaneous transluminal coronary angioplasty (PTCA) or

    balloon angioplasty.

    Angioplasty may be a planned procedure for someone with angina, or an urgent treatment if the symptoms have become unstable.

    Having a coronary angiogram (a type of X-ray used to check blood vessels) will determine if you're suitable for treatment.

    Coronary angioplasty is also performed as an emergency treatment during a heart attack.

    During the procedure, a small balloon is inserted to push the fatty tissue in the narrowed artery outwards. This allows the blood to

    flow more easily. A metal stent (a wire mesh tube) is usually placed in the artery to hold it open. Drug-eluting stents can also be used.

    These release medicines to stop the artery narrowing again.

    CORONARY ARTERY BYPASS GRAFT

    Coronary artery bypass grafting (CABG) is also known as bypass surgery, a heart bypass, or coronary artery bypass surgery.

    It's carried out in people whose arteries are narrowed or blocked.

    A coronary angiogram will determine if you're suitable for treatment.

    Off-pump coronary artery bypass (OPCAB) is a type of coronary artery bypass surgery. It's performed while the heart continues to pump blood

    by itself without the need for a heart-lung machine. A blood vessel is inserted (grafted) between the main artery leaving the heart

    (the aorta) and a part of the coronary artery beyond the narrowed or blocked area

    Sometimes, an artery that supplies blood to the chest wall is used and diverted to one of the heart arteries. This allows the blood to

    bypass (get around) the narrowed sections of coronary arteries.

    HEART TRANSPLANT

    Occasionally, when the heart is severely damaged and medicine is not effective, or when the heart becomes unable to adequately pump blood

    around the body (heart failure), a heart transplant may be needed.

    A heart transplant involves replacing a heart that's damaged or is not working properly with a healthy donor heart.

    It's possible to lead a normal life after having heart surgery or problems like a heart attack.

    CARDIAC REHABILITATION PROGRAMME

    If you have heart surgery, a member of the cardiac rehabilitation team may visit you in hospital to give you information about your

    condition and the procedure you're having.

    This care will usually continue after you've left hospital. For the first few weeks after your surgery, a member of the cardiac

    rehabilitation team may visit you at home or call you to check on your progress. Cardiac rehabilitation programmes can vary widely

    throughout the country, but most will cover the following basic areas:

    1.  exercise
    2.  education
    3.  relaxation and emotional support

    Once you've completed your rehabilitation programme, it's important to exercise regularly and lead a healthy lifestyle. This will help

    protect your heart and reduce the risk of further heart-related problems.

    HEALTH AND FITNESS

    SELF CARE

    Self-care is an integral part of daily life, and is all about you taking responsibility for your own health and wellbeing with the

    support of those involved in your care. Self-care includes actions you take for yourself every day so you stay fit and maintain good

    physical and mental health. It also helps you to prevent illness or accidents and care more effectively for minor ailments and long-term

    conditions. People living with long-term conditions can benefit enormously from being supported so they can achieve self-care. They can

    live longer, have less pain, anxiety, depression and fatigue, have a better quality of life, and be more active and independent.

    SUPPORT GROUPS

    If you have a heart condition, or if you're caring for someone with a heart condition, you might find it useful to meet other people in

    your area who are in a similar situation. There are a number of heart support groups around the UK that organise regular exercise sessions,

    such as walking groups, as well as other social activities. A GP or specialist can provide you with details about your nearest group.

    RELATIONSHIPS AND SEX

    Coming to terms with a long-term condition such as heart disease can put a strain on you, your family and your friends. It can be difficult

    to talk to people about your condition, even if they're close to you.

    Be open about how you feel and let your family and friends know what they can do to help. But do not feel shy about telling them you need

    some time to yourself.
    
                  """
        self.txt.insert(tk.END, outline)

class prescription():
    def __init__(self, Apps):
        self.Apps = Apps
        self.frame = tk.Frame(self.Apps)
        self.Apps.geometry("1225x700")
        self.Apps.tk.call('wm', 'iconphoto', Apps._w, tk.PhotoImage(file='coronry_icon.png'))
        #self.Apps.title("Available Courses")
        self.Lbl = tk.Label(self.Apps, text = 'Medical PRESCRIPTION', bg="chocolate1", fg='white', width="600", height="2")
        self.Lbl.pack(side='top')

        self.txt = tk.Text(self.Apps, height=50, width=100)
        self.txt.pack(side='left', expand='yes', fill='both')
        self.scroll = tk.Scrollbar(self.Apps, orient=tk.VERTICAL)
        self.scroll.config(command=self.txt.yview)
        self.txt.config(yscrollcommand=self.scroll.set)
        self.txt.config(font=('Times New Roman', 16))
        self.scroll.pack(side='right', ipady=330)

        outline = """
        Varous drugs can be prescriped or used to treat coronary heart disease, including

        1.  Cholesterol-modiffying medications.

        2.  Asprin

        3. Beta Blockers

        4. Calcium Channel Blockers

        5.  Ranolazine
        
                  """
        self.txt.insert(tk.END, outline)

class pharmacy():
    def __init__(self, Apps):
        self.Apps = Apps
        self.frame = tk.Frame(self.Apps)
        self.Apps.geometry("1225x700")
        self.Apps.tk.call('wm', 'iconphoto', Apps._w, tk.PhotoImage(file='coronry_icon.png'))
        #self.Apps.title("Available Courses")
        self.Lbl = tk.Label(self.Apps, text = 'PHARMACEUTICAL DRUGS', bg="chocolate1", fg='white', width="600", height="2")
        self.Lbl.pack(side='top')

        self.txt = tk.Text(self.Apps, height=50, width=100)
        self.txt.pack(side='left', expand='yes', fill='both')
        self.scroll = tk.Scrollbar(self.Apps, orient=tk.VERTICAL)
        self.scroll.config(command=self.txt.yview)
        self.txt.config(yscrollcommand=self.scroll.set)
        self.txt.config(font=('Times New Roman', 16))
        self.scroll.pack(side='right', ipady=330)

        outline = """
            1. STATINS — TO LOWER LDL CHOLESTEROL

            Statins were first introduced in 1987 and doctors now have seven different medications 

            from which to choose depending on a patient’s need. They lower the “bad”

            LDL cholesterol levels by 20 to 60% and also reduce inflammation. 

            Most people who have had a heart attack or stroke, bypass surgery, stents, 

            or diabetes should be taking statins. Some patients with a high LDL level, but 

            without heart disease, should also take statins.

            2. ASPIRIN — TO PREVENT BLOOD CLOTS

            Aspirin has been around for a long time and was first discovered to have 

            cardiovascular benefits in the 1960s. Aspirin can help to keep your arteries 

            open because of its anti-clotting and anti-platelet effects. A standard dosage for

            heart patients are 81 mg a day, which is one baby aspirin. Aspirin makes sense for

            who already have heart disease, but not necessarily for people who just have risk factors.

            But cardiologist Leslie Cho, MD, advises “we should emphasize that it’s really 
    
            not recommended for primary prevention unless the ischemic benefit outweighs the bleeding risk.”
        
            3. CLOPIDOGREL — TO PREVENT BLOOD CLOTS

            This drug is considered a “super-aspirin” because of its effectiveness in preventing

            platelet clumping, and it’s often used in combination with aspirin. 

            For some patients there is an increased risk of bleeding and doctors will weigh 

            the benefits versus the risks of this drug. However, if you have a stent, 

            the combination of aspirin and clopidogrel is essential to preventing clotting. 

            It’s also often used for patients with worsening angina.

            Dr. Cho says if you’ve had acute coronary syndrome, a better option might 

            be Ticagrelor or Prasugrel, however.

            4. WARFARIN — TO PREVENT BLOOD CLOTS

            This drug is a stronger anti-clotting agent than aspirin and clopidogrel. 

            It works as an anticoagulant – or blood thinner. Warfarin was widely used in 

            the past to prevent the formation of clots if you have atrial fibrillation, an 

            artificial heart valve or if you have blood clots in your legs.

            Dr. Cho says now Warfarin is no longer the first line medication choice for afib 

            or a blood clot in the leg or lungs. It’s primarily used for heart valve disease.

            And because it interacts with other medications and diet, it requires close monitoring by a physician.

            “The first line drug for afib (depending on renal function) is novel oral anticoagulants,” she says.

            5. Beta-blockers — to treat heart attack and heart failure and sometimes used to 

            lower blood pressure. Beta-blockers block the effects of adrenaline, which comes 

            on in response to stressful situations. Beta-blockers are prescribed in the treatment of these four conditions:

            Angina.

            Heart attack.

            Congestive heart failure.

            Abnormal heart rhythms.

            Dosage of these medications must be adjusted for the desired response. 

            Your doctor will monitor you for dizziness (due to low heart rate) kidney and liver problems.

            6. ACE INHIBITORS — TO TREAT HEART FAILURE AND LOWER BLOOD PRESSURE

            ACE (angiotensin-converting enzyme) inhibitors prevent the body from producing 

            the artery-constricting hormone angiotensin. Arteries relax with ACE inhibitors and

            this lowers blood pressure. They are prescribed for patients with congestive heart failure, 

            a recent heart attack, and those with hypertension.

            Collectively, these drugs save lives by preventing heart attacks and strokes. 

            Chances are you will take one or more of these medications if you are at risk for or

            have coronary heart disease. Be sure to know your medications and follow your 

            doctor’s instructions. You’ll want to work with them to get the safe and effective combination for you.     
                  """
        self.txt.insert(tk.END, outline)
        
class Causes():
    def __init__(self, Apps):
        self.Apps = Apps
        self.frame = tk.Frame(self.Apps)
        self.Apps.geometry("1225x700")
        self.Apps.tk.call('wm', 'iconphoto', Apps._w, tk.PhotoImage(file='coronry_icon.png'))
        #self.Apps.title("Available Courses")
        self.Lbl = tk.Label(self.Apps, text = 'CAUSES OF CHD', bg="chocolate1", fg='white', width="600", height="2")
        self.Lbl.pack(side='top')

        self.txt = tk.Text(self.Apps, height=50, width=100)
        self.txt.pack(side='left', expand='yes', fill='both')
        self.scroll = tk.Scrollbar(self.Apps, orient=tk.VERTICAL)
        self.scroll.config(command=self.txt.yview)
        self.txt.config(yscrollcommand=self.scroll.set)
        self.txt.config(font=('Times New Roman', 16))
        self.scroll.pack(side='right', ipady=330)

        outline = """
    Coronary heart disease (CHD) is usually caused by a build-up of fatty deposits (atheroma) on the walls of the arteries around

    the heart (coronary arteries). The build-up of atheroma makes the arteries narrower, restricting the flow of blood to the heart muscle.

    This process is called atherosclerosis. Your risk of developing atherosclerosis is significantly increased if you:

    SMOKE

    have high blood pressure (hypertension)

    have high cholesterol

    have high levels of lipoprotein (a)

    do not exercise regularly

    HAVE DIABETES

    Other risk factors for developing atherosclerosis include:

    BEING OBESE OR OVERWEIGHT

    having a family history of CHD – the risk is increased if you have a male relative under the age of 55, or a female relative under 65, with CHD

    Smoking

    Smoking is a major risk factor for coronary heart disease. Both nicotine and carbon monoxide (from the smoke) put a strain on the heart

    by making it work faster. They also increase your risk of blood clots.

    Other chemicals in cigarette smoke can damage the lining of your coronary arteries, leading to furring of the arteries.

    Smoking significantly increases your risk of developing heart disease.

    HIGH BLOOD PRESSURE

    High blood pressure (hypertension) puts a strain on your heart and can lead to CHD.

    Blood Pressure UK have also produced a useful guide explaining high, low and normal blood pressure readings.   

    HIGH CHOLESTEROL

    Cholesterol is a fat made by the liver from the saturated fat in your diet. It's essential for healthy cells, but too much in the

    blood can lead to CHD.

    HIGH LIPOPROTEIN (A)

    Like cholesterol, lipoprotein (a), also known as LP(a), is a type of fat made by the liver. It's a known risk factor for cardiovascular

    disease and atherosclerosis. The level of LP(a) in your blood is inherited from your parents. It's not routinely measured, but

    screening is recommended for people with a moderate or high risk of developing cardiovascular disease.

    LACK OF REGULAR EXERCISE

    If you're inactive, fatty deposits can build up in your arteries.

    If the arteries that supply blood to your heart become blocked, it can lead to a heart attack. If the arteries that supply blood to your

    brain are affected it can cause a stroke.

    DIABETES

    A high blood sugar level may lead to diabetes, which can more than double your risk of developing CHD.

    Diabetes can lead to CHD because it may cause the lining of blood vessels to become thicker, which can restrict blood flow.

    THROMBOSIS

    A thrombosis is a blood clot in a vein or artery.

    If a thrombosis develops in a coronary artery it prevents the blood supply from reaching the heart muscle. This usually leads to a heart attack.
                                                                      
                  """
        self.txt.insert(tk.END, outline)


#defmain():
 #   root =tk.Tk()
  #  app = Medical_App(root)
   # app.pack(side="top")



def center_window(w=10000, h=700):
    root =tk.Tk()
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='coronry_icon.png'))

    app = Medical_App(root)

if __name__ == '__main__':
    center_window(1200, 650)
    
#root = tk.Tk()
#center_window(1200, 650)
#root.mainloop()


        
