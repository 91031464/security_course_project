from django import template
from ..models import Agent

register = template.Library()

@register.inclusion_tag('agent_check.html')
def is_agent(user_name):
    agents = Agent.objects.all()
    agents_names = []
    valid_agent = False

    for agent in agents:
        agents_names.append(agent.agent_username)
    
    if user_name in agents_names:
        valid_agent = True
    
    return {'valid_agent': valid_agent}
