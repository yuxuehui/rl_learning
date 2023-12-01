import re
save_prefix = 'pickandplace_mass10_height0.07-0.18'
with open('/home/llm_user/index/rl_learning/PandaPickAndPlace_mass_10_2023-11-08 14:04:45.out','r',encoding='utf-8') as f:
    data = f.read()
    actor_loss = re.findall(r'actor_loss.*?\|(.*?)\|',data)
    critic_loss = re.findall(r'critic_loss.*?\|(.*?)\|',data)
    success_rate = re.findall(r'success_rate.*?\|(.*?)\|',data)

    actor_loss = [float(loss.strip()) for loss in actor_loss]
    critic_loss = [float(loss.strip()) for loss in critic_loss]
    success_rate = [float(rate.strip()) for rate in success_rate]


import matplotlib.pyplot as plt
import numpy as np
titles = ['actor_loss','critic_loss','success_rate']
for title in titles:
    
    if title == 'success_rate':
        xlabel = 'episodes'
        t = np.arange(0, len(success_rate)) * 4
    else:
        xlabel = 'n_updates'
        t = np.arange(0, len(critic_loss))

    actor_loss = np.array(actor_loss)
    critic_loss = np.array(critic_loss)
    success_rate = np.array(success_rate)

    fig, ax = plt.subplots()
    ax.plot(t, eval(title))

    ax.set(xlabel=xlabel, ylabel=f'{title}',
        title=f'{title}')

    ax.grid()

    fig.savefig(f"{save_prefix}_{title}.png")
    plt.show()